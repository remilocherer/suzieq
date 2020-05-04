from suzieq.sqobjects import *
import streamlit as st
import pandas as pd

# df['prefix'] = df.prefix.astype(str)


def get_df(sqobject, **kwargs):
    view = kwargs.pop('view', 'latest')

    return sqobject(view=view).get(**kwargs)


def color_row(row, **kwargs):
    """Color the appropriate column red if the status has failed"""
    fieldval = kwargs.pop("fieldval", "down")
    field = kwargs.pop("field", "state")
    color = kwargs.pop("color", "red")
    if row[field] == fieldval:
        return [f"background-color: {color}"]*len(row)
    else:
        return [""]*len(row)


def color_element_red(value, **kwargs):
    fieldval = kwargs.pop("fieldval", "down")
    if value in fieldval:
        return "color: green"
    else:
        return "color: red"


def style(df, table):
    """Apply appropriate styling for the dataframe based on the table"""
    if table == 'bgp':
        return df.style.applymap(color_element_red, fieldval=['Established'],
                                 subset=pd.IndexSlice[:, ['state']])
    elif table == 'ospf':
        return df.style.applymap(color_element_red,
                                 fieldval=["full", "passive"],
                                 subset=pd.IndexSlice[:, ['adjState']])
    elif table == "routes":
        return df.style.apply(color_row, axis=1, fieldval='0.0.0.0/0',
                              field='prefix', color='yellow')
    elif table == "interfaces":
        return df.style.applymap(color_element_red, fieldval=["up"],
                                 subset=pd.IndexSlice[:, ['state']])
    else:
        return df

def _main():

    st.title('Suzieq')

    sqobj = {
        'address': address.AddressObj,
        'arpnd': arpnd.ArpndObj,
        'bgp': bgp.BgpObj,
        'device': device.DeviceObj,
        'interfaces': interfaces.IfObj,
        'lldp': lldp.LldpObj,
        'macs': macs.MacsObj,
        'ospf': ospf.OspfObj,
        'routes': routes.RoutesObj
    }

    option = st.sidebar.selectbox(
        'Select Table to View', tuple(sqobj.keys()))
    view = st.sidebar.radio("View of Data", ('latest', 'all'))
    columns = st.sidebar.text_input("Columns to View (default, all or space separated list",
                                    value='default')
    filter = st.sidebar.text_input(
        'Filter results with pandas query', value='')
    st.sidebar.markdown(
        "[query syntax help](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)")

    if columns == 'all':
        columns = '*'
    df = get_df(sqobj[option], view=view, columns=[columns])

    if not df.empty:
        if filter:
            df1 = df.query(filter)
        else:
            df1 = df
        st.subheader(f'{option} View')
        convert_dict = {x: 'str' for x in df.select_dtypes('category').columns}
        if option == 'routes':
            df1['prefix'] = df1.prefix.astype(str)
        elif option == 'macs':
            df1.drop(columns=['mackey'], inplace=True)
        st.dataframe(data=style(df1.astype(convert_dict), option),
                     height=600, width=2500)
        st.sidebar.subheader(f'{option} column names')
        st.sidebar.table(tables.TablesObj().describe(
            table=option).style.hide_index())


if __name__ == '__main__':
    _main()
