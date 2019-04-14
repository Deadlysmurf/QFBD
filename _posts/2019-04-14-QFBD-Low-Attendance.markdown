---
layout: post
title: Question for the Baseball Database: What's the lowest Blue Jay attendance?
categories: Baseball, QFBD
---

## The Question: "What's the lowest attendance on record for the Blue Jays?"

At one of the first games of the 2019 baseball season, my parents were going to the game and the stadium was *empty*. We know that the game before had had the lowest attendance since 2009, but when we were placing bets on how low it would go for that game, we realized we didn't know what the actual floor was.

"I could look up the data?" - Me

Thus started this blog series.

## The Data

I peaked into the Lahman database and didn't see exactly the table that I wanted to look at, so I used the the [pybaseball package](https://github.com/jldbc/pybaseball) to download the data I needed. I'm pretty sure this table comes from [baseball-reference](www.baseball-reference.com)

```
years = range(1977, 2019)

output_data = pd.DataFrame()

for i in years:
    data_load = pybaseball.schedule_and_record(i, 'TOR')
    data_load['Year'] = i
    output_data = pd.concat([output_data, data_load], axis=0, join='outer', join_axes=None, ignore_index=True)
```

Was this a sloppy way to pull this data? Probably - but I only had 20 minutes to game time, so it worked and I moved on.


## Data Prep
The prep for this question was pretty easy, there were only a handful of filters to apply to the data to get it ready.

#### Home Games
The data included all home and away games for the Toronto Blue Jays. We only care about home games to answer this question, so I filtered to only include the home games.

```
home_only = raw_data[raw_data['Home_Away'] == 'Home']
```

#### Double Headers
Double headers often allow people with tickets to attend one game attend both of the games. The attendance for the first game doesn't appear to be recorded in the data set, because it comes back with 'Not a number'. Rather than have them clutter things up, I'd rather drop them off.

```
home_only = home_only.dropna(subset=['Attendance'])
```

#### Sort it out
We want to know the games with the lowest attendance, so we need to sort by the attendance.

```
home_only.sort_values('Attendance', inplace=True)
```
## Final Answer

```
print(home_only.head())
```

Date |   Tm|  Opp|  Attendance
---|---|---|---
Tuesday, Apr 17  1979|  TOR|  CHW|     10074.0
Tuesday, Apr 13  1982|  TOR|  DET|     10087.0
Tuesday, Apr 27  1982|  TOR|  TEX|     10101.0
Friday, Apr 21  1978|  TOR|  CHW|     10108.0
Wednesday, Apr 28  1982|  TOR|  TEX|     10109.0

The lowest attendance on record is 10,074 on April 17th, 1979. According to wikipedia, this season was not a good season: "The Blue Jays were the only American League East team to finish 1979 with a losing record and the loss total of 109 set the franchise mark." April would have been too early for fans to know it was going to be this bad, but it's nice that they set the record for lowest attendance and loss total in the same season.

[The python script can be found here](https://github.com/Deadlysmurf/QFBD/blob/master/src/2019_04_14_QFBD_Attendance.py)
