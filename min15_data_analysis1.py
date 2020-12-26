import pandas as pd
import datetime

#read this article
#https://www.eia.gov/todayinenergy/detail.php?id=42915
df=pd.read_csv('Demo_Electric_15_Minute_05-16-2018_06-16-2019_20190618051449472.csv',skiprows=14)
df['timestamp']=(df['Date']+' '+df['Start Time']).map(lambda x: datetime.datetime.strptime(x,'%m/%d/%Y %I:%M %p'))
#You use datetime twice because first you use datetime object that you imported and then you use the method datetime
#Alternatively you can import the datetime object from the module:
    #from datetime import datetime
    #dtDate = datetime.strptime(sDate, "%m/%d/%Y")
df['month']=df['timestamp'].map(lambda x: x.month)
df['season']='summer'
df.loc[df['month'].isin([11,12,1,2,3,4,5]),'season']='winter'

df['hoursSinceMidnight']=df['timestamp'].map(lambda x: float(x.hour)+float(x.minute)/60.0+float(x.second)/3600.0)

print(df)

df=df.sort_values(['timestamp'])
df.to_csv('out.csv',index=False)