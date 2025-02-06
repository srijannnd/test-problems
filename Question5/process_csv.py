def get_top_recommendation(df):
    # Find the top recommendation by Broker
    df = df.loc[df.groupby('Broker')['Upside'].idxmax()]
    return df


def get_top_three(df):
    df_sorted = df.sort_values(by='Upside', ascending=False)
    top_3_df = df_sorted.head(3)
    return {"Broker": list(top_3_df["Broker"]), "Stock": list(top_3_df["Stock"])}

