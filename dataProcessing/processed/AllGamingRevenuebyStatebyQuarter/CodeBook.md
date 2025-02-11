
## AllGamingRevenuebyStatebyQuarter

### Content
U.S. commercial casino gaming revenue (GGR)

### File Name Syntax
#### tidy
- After processed; 
- Each row is an observation of each state by time. 
#### all
- Includes yearly data and quarterly data.
#### yearly
- Only includes yearly data. 
#### quarterly
- Only includes quarterly data.

### Variables
#### State
- type: object
- The full name of each state; 
- State == United States is the data of the whole country.
#### Year
- type: int32
- the year of the data.
#### Quarter
- type: object
- the quarter of the data;
- Q\d is the quarterly data;
- CY is the yearly data. 
#### Revenue
- type: float64
- The U.S. commercial casino gaming revenue of the according time.
