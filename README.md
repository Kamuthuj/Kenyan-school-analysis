The purpose of the project is to do an evaluation of the distribution of schools in Kenya based on their founders(Sponsor) and evaluate if an institution is Public or Private.

The analysis is based on the 8 Provinces in Kenya:
1.Rift Valley.
2.North Eastern.
3.Coast.
4.Western.
5.Eastern
6.Nairobi.
7.Central.
8.Nyanza.

Different stakeholders are Key players in the education industry led by Religious Organizations. Also the distribution of these learning is uneven and is dependant on various things such as demand for education and also geographical location. The Population of Kenya is highest between 0-18 years creating a high demand for ECD,Primary and Secondary education. Quality of the education is based on the status of the school(Public or Private). Private schools tend to be more prestigious than public schools hence enrollment in the private is not as high as the public ones.

At tertiary level, there are different forms of education such as public and private university education,technical training institutes,insititutes if technology and also national polytechs.These are the higher learning institutions but are very few because starting such institutions is very expensive as they have to havew diverse courses to learn making them quite expensive. In Kenya these institutions charge very high fee charges discouraging enrollment. Also the Kenyan government has tried to increase the enrollment to this institutions where they encourage students to take loans through the Higher Education Loans Board(HELB). All visualizations of school distribution by their Provinces is shown in the streamlit app.


METHODOLOGY.
I used a data set from the Ministry Of Education in Kenya. I perfomed the ETL processes and discovered that the data had various missing values where I used an imputer to fill the null values with the mode(The data was based on string values)
I dealt with the duplicates by dropping them to have a data set with Unique values.
On the column "Sponsor" I dropped sponsors whose value counts were < 10 as their contribution was minimal.
I did some feature extraction to encode some of the columns to get insights on the data as working with continous variable was much easier.
I extracted the coordinates column from the data frame to create a new data frame to easily iterate through the coordinates to create the geojson plots of the school distribution.


VIEW ON WIDE MODE.

