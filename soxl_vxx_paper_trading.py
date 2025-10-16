import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

class SOXLVXXPaperTrading:
    def __init__(self, initial_capital=100000, soxl_ratio=0.75, vxx_ratio=0.25):
        """
        SOXL-VXX 모의투자 시뮬레이터
        
        Parameters:
        - initial_capital: 초기 투자금 (기본값: $100,000)
        - soxl_ratio: SOXL 투자 비율 (기본값: 0.75 = 75%)
        - vxx_ratio: VXX 투자 비율 (기본값: 0.25 = 25%)
        """
        self.initial_capital = initial_capital
        self.soxl_ratio = soxl_ratio
        self.vxx_ratio = vxx_ratio
        
        # 포트폴리오 상태
        self.cash = initial_capital
        self.soxl_shares = 0
        self.vxx_shares = 0
        self.current_capital = initial_capital
        
        # 거래 기록
        self.trade_history = []
        self.portfolio_history = []
        self.rebalance_dates = []
        
        # 성과 지표
        self.total_return = 0
        self.annual_return = 0
        self.volatility = 0
        self.max_drawdown = 0
        self.sharpe_ratio = 0
        
    def fetch_data(self, start_date="2025-01-01", end_date="2025-12-31"):
        """SOXL과 VXX 데이터를 가져옵니다."""
        print(f"SOXL과 VXX 데이터를 수집하는 중... ({start_date} ~ {end_date})")
        
        try:
            # SOXL 데이터 수집
            soxl_data = yf.download("SOXL", start=start_date, end=end_date, progress=False)
            if soxl_data.empty:
                raise ValueError("SOXL 데이터를 가져올 수 없습니다.")
            
            # VXX 데이터 수집
            vxx_data = yf.download("VXX", start=start_date, end=end_date, progress=False)
            if vxx_data.empty:
                raise ValueError("VXX 데이터를 가져올 수 없습니다.")
            
            # MultiIndex 컬럼 처리
            if isinstance(soxl_data.columns, pd.MultiIndex):
                soxl_data.columns = soxl_data.columns.droplevel(0)
            if isinstance(vxx_data.columns, pd.MultiIndex):
                vxx_data.columns = vxx_data.columns.droplevel(0)
            
            # 컬럼명 정리
            if len(soxl_data.columns) == 6:
                soxl_data.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
            elif len(soxl_data.columns) == 5:
                soxl_data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
                
            if len(vxx_data.columns) == 6:
                vxx_data.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
            elif len(vxx_data.columns) == 5:
                vxx_data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            
            # 결합된 데이터
            self.data = pd.DataFrame({
                'Date': soxl_data.index,
                'SOXL_Close': soxl_data['Close'],
                'VXX_Close': vxx_data['Close'],
                'SOXL_Volume': soxl_data['Volume'],
                'VXX_Volume': vxx_data['Volume']
            }).dropna()
            
            print(f"데이터 수집 완료: {len(self.data)}개 거래일")
            print(f"기간: {self.data['Date'].iloc[0].strftime('%Y-%m-%d')} ~ {self.data['Date'].iloc[-1].strftime('%Y-%m-%d')}")
            
            return True
            
        except Exception as e:
            print(f"데이터 수집 중 오류 발생: {e}")
            return False
    
    def initial_investment(self, date):
        """초기 투자를 실행합니다."""
        soxl_price = self.data[self.data['Date'] == date]['SOXL_Close'].iloc[0]
        vxx_price = self.data[self.data['Date'] == date]['VXX_Close'].iloc[0]
        
        # 초기 투자금 배분
        soxl_investment = self.cash * self.soxl_ratio
        vxx_investment = self.cash * self.vxx_ratio
        
        # 주식 수 계산
        self.soxl_shares = soxl_investment / soxl_price
        self.vxx_shares = vxx_investment / vxx_price
        self.cash = 0
        
        # 거래 기록
        self.trade_history.append({
            'Date': date,
            'Type': 'Initial Investment',
            'SOXL_Shares': self.soxl_shares,
            'VXX_Shares': self.vxx_shares,
            'SOXL_Price': soxl_price,
            'VXX_Price': vxx_price,
            'Cash': self.cash
        })
        
        print(f"초기 투자 완료 ({date.strftime('%Y-%m-%d')})")
        print(f"SOXL: {self.soxl_shares:.2f}주 @ ${soxl_price:.2f} = ${soxl_investment:,.2f}")
        print(f"VXX: {self.vxx_shares:.2f}주 @ ${vxx_price:.2f} = ${vxx_investment:,.2f}")
    
    def calculate_portfolio_value(self, date):
        """특정 날짜의 포트폴리오 가치를 계산합니다."""
        row = self.data[self.data['Date'] == date]
        if row.empty:
            return 0
        
        soxl_price = row['SOXL_Close'].iloc[0]
        vxx_price = row['VXX_Close'].iloc[0]
        
        portfolio_value = (self.soxl_shares * soxl_price + 
                          self.vxx_shares * vxx_price + 
                          self.cash)
        
        return portfolio_value
    
    def rebalance_portfolio(self, date, target_soxl_ratio=0.75, target_vxx_ratio=0.25):
        """포트폴리오를 리밸런싱합니다."""
        current_value = self.calculate_portfolio_value(date)
        if current_value == 0:
            return
        
        row = self.data[self.data['Date'] == date]
        if row.empty:
            return
        
        soxl_price = row['SOXL_Close'].iloc[0]
        vxx_price = row['VXX_Close'].iloc[0]
        
        # 목표 주식 수 계산
        target_soxl_value = current_value * target_soxl_ratio
        target_vxx_value = current_value * target_vxx_ratio
        
        target_soxl_shares = target_soxl_value / soxl_price
        target_vxx_shares = target_vxx_value / vxx_price
        
        # 거래 실행
        soxl_diff = target_soxl_shares - self.soxl_shares
        vxx_diff = target_vxx_shares - self.vxx_shares
        
        # 주식 수 업데이트
        self.soxl_shares = target_soxl_shares
        self.vxx_shares = target_vxx_shares
        
        # 거래 기록
        self.trade_history.append({
            'Date': date,
            'Type': 'Rebalance',
            'SOXL_Shares': self.soxl_shares,
            'VXX_Shares': self.vxx_shares,
            'SOXL_Price': soxl_price,
            'VXX_Price': vxx_price,
            'Cash': self.cash,
            'SOXL_Change': soxl_diff,
            'VXX_Change': vxx_diff
        })
        
        self.rebalance_dates.append(date)
        
        print(f"리밸런싱 완료 ({date.strftime('%Y-%m-%d')})")
        print(f"포트폴리오 가치: ${current_value:,.2f}")
        print(f"SOXL: {self.soxl_shares:.2f}주 ({soxl_diff:+.2f})")
        print(f"VXX: {self.vxx_shares:.2f}주 ({vxx_diff:+.2f})")
    
    def run_simulation(self, rebalance_frequency='monthly'):
        """
        모의투자 시뮬레이션을 실행합니다.
        
        Parameters:
        - rebalance_frequency: 리밸런싱 주기 ('monthly', 'quarterly')
        """
        if not hasattr(self, 'data') or self.data.empty:
            print("먼저 데이터를 가져와주세요.")
            return
        
        print(f"\n=== SOXL-VXX 모의투자 시뮬레이션 시작 ===")
        print(f"초기 투자금: ${self.initial_capital:,.2f}")
        print(f"포트폴리오 비율: SOXL {self.soxl_ratio:.1%}, VXX {self.vxx_ratio:.1%}")
        print(f"리밸런싱 주기: {rebalance_frequency}")
        
        # 첫 번째 거래일에 초기 투자
        first_date = self.data['Date'].iloc[0]
        self.initial_investment(first_date)
        
        # 리밸런싱 날짜 계산
        if rebalance_frequency == 'monthly':
            rebalance_dates = pd.date_range(start=first_date, end=self.data['Date'].iloc[-1], freq='MS')[1:]
        elif rebalance_frequency == 'quarterly':
            rebalance_dates = pd.date_range(start=first_date, end=self.data['Date'].iloc[-1], freq='QS')[1:]
        else:
            rebalance_dates = []
        
        # 실제 거래일과 매칭
        actual_rebalance_dates = []
        for rebalance_date in rebalance_dates:
            # 리밸런싱 날짜 이후의 첫 번째 거래일 찾기
            available_dates = self.data[self.data['Date'] > rebalance_date]['Date']
            if not available_dates.empty:
                actual_rebalance_dates.append(available_dates.iloc[0])
        
        # 리밸런싱 실행
        for rebalance_date in actual_rebalance_dates:
            if rebalance_date in self.data['Date'].values:
                self.rebalance_portfolio(rebalance_date)
        
        # 일일 포트폴리오 가치 기록
        for _, row in self.data.iterrows():
            date = row['Date']
            portfolio_value = self.calculate_portfolio_value(date)
            
            self.portfolio_history.append({
                'Date': date,
                'Portfolio_Value': portfolio_value,
                'SOXL_Value': self.soxl_shares * row['SOXL_Close'],
                'VXX_Value': self.vxx_shares * row['VXX_Close'],
                'Cash': self.cash,
                'SOXL_Price': row['SOXL_Close'],
                'VXX_Price': row['VXX_Close']
            })
        
        self.portfolio_history = pd.DataFrame(self.portfolio_history)
        
        # 성과 지표 계산
        self.calculate_performance_metrics()
        
        print(f"\n=== 시뮬레이션 완료 ===")
        self.print_performance_summary()
    
    def calculate_performance_metrics(self):
        """성과 지표를 계산합니다."""
        if self.portfolio_history.empty:
            return
        
        # 기본 지표
        final_value = self.portfolio_history['Portfolio_Value'].iloc[-1]
        self.total_return = (final_value - self.initial_capital) / self.initial_capital
        
        # 연간 수익률
        days = (self.portfolio_history['Date'].iloc[-1] - self.portfolio_history['Date'].iloc[0]).days
        years = days / 365.25
        self.annual_return = (final_value / self.initial_capital) ** (1/years) - 1
        
        # 변동성 (일간 수익률 기준)
        daily_returns = self.portfolio_history['Portfolio_Value'].pct_change().dropna()
        self.volatility = daily_returns.std() * np.sqrt(252)
        
        # 최대 낙폭
        cumulative = (1 + daily_returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        self.max_drawdown = drawdown.min()
        
        # 샤프 비율 (무위험 수익률 3% 가정)
        risk_free_rate = 0.03
        self.sharpe_ratio = (self.annual_return - risk_free_rate) / self.volatility if self.volatility > 0 else 0
    
    def print_performance_summary(self):
        """성과 요약을 출력합니다."""
        final_value = self.portfolio_history['Portfolio_Value'].iloc[-1]
        
        print(f"\n포트폴리오 성과 요약")
        print(f"{'='*50}")
        print(f"초기 투자금: ${self.initial_capital:,.2f}")
        print(f"최종 가치: ${final_value:,.2f}")
        print(f"총 수익: ${final_value - self.initial_capital:,.2f}")
        print(f"총 수익률: {self.total_return:.2%}")
        print(f"연간 수익률: {self.annual_return:.2%}")
        print(f"연간 변동성: {self.volatility:.2%}")
        print(f"최대 낙폭: {self.max_drawdown:.2%}")
        print(f"샤프 비율: {self.sharpe_ratio:.3f}")
        
        # 리밸런싱 정보
        print(f"\n리밸런싱 정보")
        print(f"{'='*50}")
        print(f"리밸런싱 횟수: {len(self.rebalance_dates)}회")
        for i, date in enumerate(self.rebalance_dates, 1):
            print(f"{i}. {date.strftime('%Y-%m-%d')}")
    
    def create_visualizations(self):
        """시각화를 생성합니다."""
        if self.portfolio_history.empty:
            print("포트폴리오 데이터가 없습니다.")
            return
        
        figures = []
        
        # 1. 포트폴리오 가치 변화
        fig1 = go.Figure()
        
        fig1.add_trace(go.Scatter(
            x=self.portfolio_history['Date'],
            y=self.portfolio_history['Portfolio_Value'],
            mode='lines',
            name='포트폴리오 가치',
            line=dict(color='blue', width=3)
        ))
        
        # 리밸런싱 날짜는 별도로 표시하지 않음 (Plotly 호환성 문제)
        
        fig1.update_layout(
            title='SOXL-VXX 포트폴리오 가치 변화 (75% SOXL, 25% VXX)',
            xaxis_title='날짜',
            yaxis_title='포트폴리오 가치 ($)',
            height=500
        )
        
        figures.append(fig1)
        
        # 2. 자산별 가치 변화
        fig2 = go.Figure()
        
        fig2.add_trace(go.Scatter(
            x=self.portfolio_history['Date'],
            y=self.portfolio_history['SOXL_Value'],
            mode='lines',
            name='SOXL 가치 (75%)',
            line=dict(color='green', width=2)
        ))
        
        fig2.add_trace(go.Scatter(
            x=self.portfolio_history['Date'],
            y=self.portfolio_history['VXX_Value'],
            mode='lines',
            name='VXX 가치 (25%)',
            line=dict(color='red', width=2)
        ))
        
        fig2.update_layout(
            title='자산별 포트폴리오 가치',
            xaxis_title='날짜',
            yaxis_title='자산 가치 ($)',
            height=500
        )
        
        figures.append(fig2)
        
        # 3. 일간 수익률
        daily_returns = self.portfolio_history['Portfolio_Value'].pct_change().dropna() * 100
        
        fig3 = go.Figure()
        
        fig3.add_trace(go.Scatter(
            x=self.portfolio_history['Date'][1:],
            y=daily_returns,
            mode='lines',
            name='일간 수익률',
            line=dict(color='purple', width=1)
        ))
        
        fig3.add_hline(y=0, line_dash="dash", line_color="black")
        
        fig3.update_layout(
            title='일간 수익률 (%)',
            xaxis_title='날짜',
            yaxis_title='수익률 (%)',
            height=400
        )
        
        figures.append(fig3)
        
        # 4. 누적 수익률
        cumulative_returns = (self.portfolio_history['Portfolio_Value'] / self.initial_capital - 1) * 100
        
        fig4 = go.Figure()
        
        fig4.add_trace(go.Scatter(
            x=self.portfolio_history['Date'],
            y=cumulative_returns,
            mode='lines',
            name='누적 수익률',
            line=dict(color='orange', width=3)
        ))
        
        fig4.add_hline(y=0, line_dash="dash", line_color="black")
        
        fig4.update_layout(
            title='누적 수익률 (%)',
            xaxis_title='날짜',
            yaxis_title='누적 수익률 (%)',
            height=400
        )
        
        figures.append(fig4)
        
        return figures
    
    def save_results(self, filename=None):
        """결과를 Excel 파일로 저장합니다."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"SOXL_VXX_Paper_Trading_{timestamp}.xlsx"
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # 포트폴리오 히스토리
            self.portfolio_history.to_excel(writer, sheet_name='Portfolio_History', index=False)
            
            # 거래 기록
            if self.trade_history:
                trade_df = pd.DataFrame(self.trade_history)
                trade_df.to_excel(writer, sheet_name='Trade_History', index=False)
            
            # 성과 요약
            summary_data = {
                '지표': [
                    '초기 투자금',
                    '최종 포트폴리오 가치',
                    '총 수익',
                    '총 수익률',
                    '연간 수익률',
                    '연간 변동성',
                    '최대 낙폭',
                    '샤프 비율',
                    '리밸런싱 횟수'
                ],
                '값': [
                    f"${self.initial_capital:,.2f}",
                    f"${self.portfolio_history['Portfolio_Value'].iloc[-1]:,.2f}",
                    f"${self.portfolio_history['Portfolio_Value'].iloc[-1] - self.initial_capital:,.2f}",
                    f"{self.total_return:.2%}",
                    f"{self.annual_return:.2%}",
                    f"{self.volatility:.2%}",
                    f"{self.max_drawdown:.2%}",
                    f"{self.sharpe_ratio:.3f}",
                    f"{len(self.rebalance_dates)}회"
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Performance_Summary', index=False)
        
        print(f"결과가 {filename}에 저장되었습니다.")
        return filename

def run_comparison_simulation():
    """다양한 리밸런싱 주기로 시뮬레이션을 비교 실행합니다."""
    print("=== SOXL-VXX 모의투자 시뮬레이션 비교 ===\n")
    
    # 시뮬레이션 설정
    initial_capital = 10000
    soxl_ratio = 0.75
    vxx_ratio = 0.25
    
    results = {}
    
    # 1개월 리밸런싱
    print("1. 1개월 리밸런싱 시뮬레이션")
    simulator_monthly = SOXLVXXPaperTrading(initial_capital, soxl_ratio, vxx_ratio)
    
    if simulator_monthly.fetch_data():
        simulator_monthly.run_simulation('monthly')
        results['monthly'] = simulator_monthly
        
        # 시각화 저장
        figures = simulator_monthly.create_visualizations()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for i, fig in enumerate(figures):
            chart_names = ['portfolio_value', 'asset_values', 'daily_returns', 'cumulative_returns']
            filename = f"monthly_{chart_names[i]}_{timestamp}.html"
            fig.write_html(filename)
            print(f"차트가 {filename}에 저장되었습니다.")
        
        # Excel 저장
        excel_filename = f"monthly_results_{timestamp}.xlsx"
        simulator_monthly.save_results(excel_filename)
    
    print("\n" + "="*80 + "\n")
    
    # 3개월 리밸런싱
    print("2. 3개월 리밸런싱 시뮬레이션")
    simulator_quarterly = SOXLVXXPaperTrading(initial_capital, soxl_ratio, vxx_ratio)
    
    if simulator_quarterly.fetch_data():
        simulator_quarterly.run_simulation('quarterly')
        results['quarterly'] = simulator_quarterly
        
        # 시각화 저장
        figures = simulator_quarterly.create_visualizations()
        
        for i, fig in enumerate(figures):
            chart_names = ['portfolio_value', 'asset_values', 'daily_returns', 'cumulative_returns']
            filename = f"quarterly_{chart_names[i]}_{timestamp}.html"
            fig.write_html(filename)
            print(f"차트가 {filename}에 저장되었습니다.")
        
        # Excel 저장
        excel_filename = f"quarterly_results_{timestamp}.xlsx"
        simulator_quarterly.save_results(excel_filename)
    
    # 비교 결과 출력
    print("\n" + "="*80)
    print("리밸런싱 주기별 성과 비교")
    print("="*80)
    
    if 'monthly' in results and 'quarterly' in results:
        monthly = results['monthly']
        quarterly = results['quarterly']
        
        print(f"{'지표':<20} {'1개월':<15} {'3개월':<15} {'차이':<15}")
        print("-" * 65)
        print(f"{'최종 가치':<20} ${monthly.portfolio_history['Portfolio_Value'].iloc[-1]:,.2f} ${quarterly.portfolio_history['Portfolio_Value'].iloc[-1]:,.2f} ${quarterly.portfolio_history['Portfolio_Value'].iloc[-1] - monthly.portfolio_history['Portfolio_Value'].iloc[-1]:,.2f}")
        print(f"{'총 수익률':<20} {monthly.total_return:.2%} {quarterly.total_return:.2%} {(quarterly.total_return - monthly.total_return):.2%}")
        print(f"{'연간 수익률':<20} {monthly.annual_return:.2%} {quarterly.annual_return:.2%} {(quarterly.annual_return - monthly.annual_return):.2%}")
        print(f"{'연간 변동성':<20} {monthly.volatility:.2%} {quarterly.volatility:.2%} {(quarterly.volatility - monthly.volatility):.2%}")
        print(f"{'최대 낙폭':<20} {monthly.max_drawdown:.2%} {quarterly.max_drawdown:.2%} {(quarterly.max_drawdown - monthly.max_drawdown):.2%}")
        print(f"{'샤프 비율':<20} {monthly.sharpe_ratio:.3f} {quarterly.sharpe_ratio:.3f} {(quarterly.sharpe_ratio - monthly.sharpe_ratio):.3f}")
        print(f"{'리밸런싱 횟수':<20} {len(monthly.rebalance_dates)}회 {len(quarterly.rebalance_dates)}회 {len(quarterly.rebalance_dates) - len(monthly.rebalance_dates)}회")
    
    return results

if __name__ == "__main__":
    # 비교 시뮬레이션 실행
    results = run_comparison_simulation()
