import sqlite3 as sql


conn = sql.connect('covid_dataset.sqlite')
c = conn.cursor()

june=c.execute("select count(new_cases) from covid where date like '2020-06%' and location='Georgia'")

def deaths(qveyana, tarigi):
    c.execute("select total_deaths from covid where location=? and date=?", (qveyana, tarigi))
    res=c.fetchone()[0]
    return res


print(deaths("Georgia","2020-06-03"))

def total():
    c.execute("select location from covid  where date='2020-06-07' order by total_deaths_per_million desc")
    res = c.fetchmany(5)
    return res

print(total())


conn.close()
