#Modules
import justpy as jp
import pandas

#Loading Data Frame
data = pandas.read_csv("market-price.csv", parse_dates=["Timestamp"])
data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()

#Linechart uses JSON (dictionary) format
line_chart = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: "Bitcoin Market Price (USD)"
    },
    subtitle: {
        text: "The average USD market price of Bitcoin in a 1 Year Duration (12/08/2021-12/08/2022)"
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: "{value} "
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: "USD"
        },
        labels: {
            format: "{value}"
        },
        accessibility: {
            rangeDescription: "k"
        },
        lineWidth: 1
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: "{point.y}$ <br>  Day: {point.x}"
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Value',
        data: [[0, 15], [70, -55.7], [80, -76.5]]
    }]
}
"""
#Application function. The function will be called at bottom of program
def application():
    #Justpy uses JS based framework 'Quasar', page function to create webpage
    web_page = jp.QuasarPage()
    #Headings for web page
    h1 = jp.QDiv(a = web_page, text="Kay's Bitcoin Web Page", classes="text-h3 text-center q-pa-md")
    highchart = jp.HighCharts(a = web_page, options = line_chart, classes="m-2 p-2 border")
    highchart.options.title.text = "Bitcoin Market Price (USD)"

    highchart.options.xAxis.categories = list(day_average.index)
    highchart.options.series[0].data = list(day_average["market-price"])
    
    return web_page

#Justpy function that takes another function as an argument. The application function contain the Quasar Page 
jp.justpy(application)