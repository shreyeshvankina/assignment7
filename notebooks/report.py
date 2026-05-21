import marimo

__generated_with = "0.8.0" 
app = marimo.App()

@app.cell
def __():
    import pandas as pd
    import matplotlib.pyplot as plt
    import marimo as mo
    return mo, pd, plt

@app.cell
def __(pd, plt):
    df = pd.read_csv("../data/features/events.csv")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df['duration_minutes'], bins=30, color='skyblue', edgecolor='black')
    
    ax.set_title('Distribution of Event Durations')
    ax.set_xlabel('Duration (Minutes)')
    ax.set_ylabel('Frequency')
    fig
    return ax, df, fig

if __name__ == "__main__":
    app.run()
