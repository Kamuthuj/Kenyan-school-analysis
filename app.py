import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
st.set_page_config(layout="wide")


st.title("School Distribution in Kenya.")
df=pd.read_csv("MOE clean data")



st.write('''The main aim of the project is to check on how education is distributed across Kenyan Provinces based on the sponsor (founder),type of school (Private or public)
         and also the different level of education offered based on the needs of the people of the different locations in the 8 Provinces of Kenya.        ''')

st.title("Distribution by the 8 provinces in Kenya .")



rift_valley=df[df["PROVINCE"]=="RIFT VALLEY"]

priv=rift_valley[rift_valley["Status"]=="PRIVATE"]
pub=rift_valley[rift_valley["Status"]=="PUBLIC"]


priv = rift_valley[rift_valley["Status"] == "PRIVATE"]
pub = rift_valley[rift_valley["Status"] == "PUBLIC"]
priv_counts = priv.groupby(["Level", "Sponsor"]).size().reset_index(name="Count")
pub_counts = pub.groupby(["Level", "Sponsor"]).size().reset_index(name="Count")
unique_sponsors = priv_counts["Sponsor"].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_counts[priv_counts["Sponsor"] == sponsor]
    pub_data = pub_counts[pub_counts["Sponsor"] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data["Count"],
        y=priv_data["Level"],
        name=f'Private - {sponsor}',
        orientation='h',
    ))

    fig.add_trace(go.Bar(
        x=pub_data["Count"],
        y=pub_data["Level"],
        name=f'Public - {sponsor}',
        orientation='h',
    ))

fig.update_layout(
    barmode='stack',
    title="1.Stacked Bar Chart: School Distribution in Rift Valley",
    xaxis_title="Count",
    yaxis_title="Level",
    legend_title="Status",
)

st.plotly_chart(fig,use_container_width=True)
st.write("Private schools: Rift valley",len(priv))
st.write("Public schools: Rift Valley",len(pub))



north_eastern=df[df["PROVINCE"]=="NORTH EASTERN"]
priv=north_eastern[north_eastern["Status"]=="PRIVATE"]
pub=north_eastern[north_eastern["Status"]=="PUBLIC"]

priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))


fig.update_layout(
    barmode='stack',
    title='2.Stacked Bar Chart: School Distribution in North Eastern Province',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)
st.plotly_chart(fig,use_container_width=True)
st.write("Private schools: North Eastern",len(priv))
st.write("Public schools: North Eastern",len(pub))


coast=df[df["PROVINCE"]=="COAST"]
priv=coast[coast["Status"]=="PRIVATE"]
pub=coast[coast["Status"]=="PUBLIC"]

priv = coast[coast["Status"] == "PRIVATE"]
pub = coast[coast["Status"] == "PUBLIC"]

priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))
fig.update_layout(
    barmode='stack',
    title='3.Stacked Bar Chart: School Distribution in Coast Province',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)

st.plotly_chart(fig,use_container_width=True)
st.write("Private schools: Coast",len(priv))
st.write("Public schools: Coast",len(pub))



western=df[df["PROVINCE"]=="WESTERN"]
priv=western[western["Status"]=="PRIVATE"]
pub=western[western["Status"]=="PUBLIC"]

priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))

fig.update_layout(
    barmode='stack',
    title='4.Stacked Bar Chart: School Distribution in Western Province',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)
st.plotly_chart(fig,use_container_width=True)
st.write("Private schools: Western",len(priv))
st.write("Public schools: Western",len(pub))


eastern=df[df["PROVINCE"]=="EASTERN"]
priv=eastern[eastern["Status"]=="PRIVATE"]
pub=eastern[eastern["Status"]=="PUBLIC"]

priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))

fig.update_layout(
    barmode='stack',
    title='5.Stacked Bar Chart: School Distribution in Eastern Province',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)
st.plotly_chart(fig,use_container_width=True)
st.write("Private schools:Eastern",len(priv))
st.write("Public schools:Eastern",len(pub))


nairobi=df[df["PROVINCE"]=="NAIROBI"]
priv=nairobi[nairobi["Status"]=="PRIVATE"]
pub=nairobi[nairobi["Status"]=="PUBLIC"]
priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))

fig.update_layout(
    barmode='stack',
    title='6.Stacked Bar Chart: School Distribution in Nairobi',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)

st.plotly_chart(fig,use_container_width=True)
st.write("Private schools: Nairobi",len(priv))
st.write("Public schools: Nairobi",len(pub))


central=df[df["PROVINCE"]=="CENTRAL"]
priv=central[central["Status"]=="PRIVATE"]
pub=central[central["Status"]=="PUBLIC"]

priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))

fig.update_layout(
    barmode='stack',
    title='7.Stacked Bar Chart: School Distribution in Central Province',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)
st.plotly_chart(fig,use_container_width=True)
st.write("Private schools: Central",len(priv))
st.write("Public schools: Central",len(pub))


nyanza=df[df["PROVINCE"]=="NYANZA"]
priv=nyanza[nyanza["Status"]=="PRIVATE"]
pub=nyanza[nyanza["Status"]=="PUBLIC"]

priv_grouped = priv.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')
pub_grouped = pub.groupby(['Level', 'Sponsor']).size().reset_index(name='Count')

unique_sponsors = priv_grouped['Sponsor'].unique()

fig = go.Figure()

for sponsor in unique_sponsors:
    priv_data = priv_grouped[priv_grouped['Sponsor'] == sponsor]
    pub_data = pub_grouped[pub_grouped['Sponsor'] == sponsor]

    fig.add_trace(go.Bar(
        x=priv_data['Count'],
        y=priv_data['Level'],
        name=f'Private - {sponsor}',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=pub_data['Count'],
        y=pub_data['Level'],
        name=f'Public - {sponsor}',
        orientation='h'
    ))

fig.update_layout(
    barmode='stack',
    title='8.Stacked Bar Chart: School Distribution in Nyanza Province',
    xaxis_title='Count',
    yaxis_title='Level',
    legend_title='Status',
)
st.plotly_chart(fig,use_container_width=True)
("Private schools:Nyanza",len(priv))
st.write("Public schools:Nyanza",len(pub))


