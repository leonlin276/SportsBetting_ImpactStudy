
## MonthlyRevenueForEachState2012to2024

### Content
Monthly gambling revenue data for each state from 2012 to 2024

### File Name Syntax
#### tidy
- After processed; 
- Each row is an observation of each state by time. 
#### all
- Includes yearly data and monthly data.
#### yearly
- Only includes yearly data; 
- Includes total data of United States from each year. 
#### monthly
- Only includes monthly data;
- Includes total data of United States from each month. 

### Variables
#### State
- type: object
- The full name of each state; 
- State == United States is the data of the whole country.
#### Year
- type: int32
- the year of the data.
#### Month
- type: object
- the month of the data;
- YTD Total is the yearly data. 
#### Date
- formatted pandas date.
#### Revenue
- type: float64
- The U.S. gambling revenue of the according time.
