# OKFGR_DM
A Python wrapper to access OKFGR data-mining server

# Quick start
```
$ git clone https://github.com/openbudgets/okfgr_dm.git
$ cd okfgr_dm
okfgr_dm $ make init
okfgr_dm $ pip3 install .
```

# Run test
```
okfgr_dm $ make test
```

# Generate documentation
```
okfgr_dm $ ./make_docu
```
Documentation is located at docs/html/

# Access OKFGR data-mining endpoint within iPython

```
$ iPython

In [1]: import okfgr_dm
In [2]: okfgr_dm.dm_okfgr("/ocpu/library/OBeU/R/ts.obeu", tsdata="Athens_draft_ts", prediction_steps=4)
```
You shall see data-mining results from OKFGR server as follows:
```
['curl', '-d', 'prediction_steps=4', '-d', 'tsdata=Athens_draft_ts', 'http://okfnrg.math.auth.gr/ocpu/library/OBeU/R/ts.obeu']
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   256    0   215  100    41    150     28  0:00:01  0:00:01 --:--:--   159
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   608    0   608    0     0    754      0 --:--:-- --:--:-- --:--:--   755
{"data_year":[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015],"data":[720895000,628937000,618550000,724830000,858942000,919508000,977488000,931607000,866517393,667108000,773422555,759559284],"predict_time":[2016,2017,2018,2019],"predict_values":[913974326.4927,913820467.8176,959478495.1833,868153360.9067],"up80":[1014507280.1335,1044499357.6016,1122438542.4075,1033064392.7714],"low80":[813441372.8519,783141578.0335,796518447.9592,703242329.0419],"up95":[1067726211.0778,1113676583.1722,1208704380.4816,1120363019.7283],"low95":[760222441.9076,713964352.4629,710252609.8851,615943702.0851]}
```
