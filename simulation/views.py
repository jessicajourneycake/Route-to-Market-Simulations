from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os


def home(chart):

    return render(chart, "index.html")


def engage(chart):
    directory = os.getcwd() + "/simulation/engage_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    eng_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/engage_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    eng_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/engage_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    eng_own = plot(fig, output_type='div')

    return render(chart, "engage.html", context={'eng_sector': eng_sector, 'eng_loc': eng_loc, 'eng_own': eng_own})


def qualify(chart):
    directory = os.getcwd() + "/simulation/qualify_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    qual_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/qualify_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    qual_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/qualify_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    qual_own = plot(fig, output_type='div')

    return render(chart, "qualify.html", context={'qual_sector': qual_sector, 'qual_loc': qual_loc, 'qual_own': qual_own})


def design(chart):
    directory = os.getcwd() + "/simulation/design_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    des_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/design_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    des_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/design_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    des_own = plot(fig, output_type='div')

    return render(chart, "design.html", context={'des_sector': des_sector, 'des_loc': des_loc, 'des_own': des_own})


def propose(chart):
    directory = os.getcwd() + "/simulation/propose_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    prop_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/propose_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    prop_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/propose_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    prop_own = plot(fig, output_type='div')

    return render(chart, "propose.html", context={'prop_sector': prop_sector, 'prop_loc': prop_loc, 'prop_own': prop_own})


def negotiate(chart):
    directory = os.getcwd() + "/simulation/negotiate_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    neg_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/negotiate_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    neg_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/negotiate_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    neg_own = plot(fig, output_type='div')

    return render(chart, "negotiate.html", context={'neg_sector': neg_sector, 'neg_loc': neg_loc, 'neg_own': neg_own})


def closing(chart):
    directory = os.getcwd() + "/simulation/closing_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    close_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/closing_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    close_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/closing_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    close_own = plot(fig, output_type='div')

    return render(chart, "closing.html", context={'close_sector': close_sector, 'close_loc': close_loc, 'close_own': close_own})


def won(chart):
    directory = os.getcwd() + "/simulation/won_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    won_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/won_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    won_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/won_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    won_own = plot(fig, output_type='div')

    return render(chart, "won.html", context={'won_sector': won_sector, 'won_loc': won_loc, 'won_own': won_own})


def loss(chart):
    directory = os.getcwd() + "/simulation/loss_sector.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Sector'],
                      values='Count', width=600, height=500)
    loss_sector = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/loss_location.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Location'],
                      values='Count', width=600, height=500)
    loss_loc = plot(fig, output_type='div')

    directory = os.getcwd() + "/simulation/loss_owner.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Changes', 'Owner'],
                      values='Count', width=600, height=500)
    loss_own = plot(fig, output_type='div')

    return render(chart, "loss.html", context={'loss_sector': loss_sector, 'loss_loc': loss_loc, 'loss_own': loss_own})


def simulations(chart):
   
    directory = os.getcwd() + "/simulation/temp.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
  
    fig = px.bar(df, x="Changes", y="Count", range_y=[0,150], animation_frame="Date", color="Status", category_orders={"Changes": [
                    "Engage", "Qualify", "Design", "Propose", "Negotiate", "Closing", "Won", "Loss"]}, height=600, width=1100)

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 3000
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 400

    bar = plot(fig, output_type='div')


    return render(chart, "simulation.html", context={'bar': bar})

def simulation2(chart):
    directory = os.getcwd() + "/simulation/funnel_output.xlsx"
    data = pd.read_excel(directory)
    df = pd.DataFrame(data)
    names=["Loss", "Won", "Closing", "Negotiate", "Propose", "Design", "Qualify", "Engage"]
    fig = px.funnel(df, x="Average", y="Changes", animation_frame="Date", category_orders={"Changes": [
                    "Loss", "Won", "Closing", "Negotiate", "Propose", "Design", "Qualify", "Engage"]}, height=600, width=900)

    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 400

    funnel = plot(fig, output_type='div')




    return render(chart, "simulation_funnel.html", context={'funnel': funnel})
