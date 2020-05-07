## Quick Start

We want to make it as easy as possible for you to start engaging with Suzieq. To that end, the quickest 
way to start is to download the docker image from github and also download the data we've already gathered 
for the 18 or so network scenarios from the [github](https://github.com/netenglabs/suzieq-data) 
repository associated with Dinesh's book, Cloud Native Data Center Networking. You can 
then use the introductory documentation to start exploring the data.

- `docker run -it --name suzieq ddutt/suzieq-demo`
- `suzieq-cli`

When you're within the suzieq-cli, you can run ```device unique columns=namespace``` to see 
the list of different scenarios, we've gathered data for.

If you're looking for more than just a demo, and would like to explore even more data that we've 
gathered, from all all scenarios listed in Dinesh's book, Cloud Native Data Center Networking, 
then use the following sequence of commands.

- ```git clone https://github.com/netenglabs/suzieq-data.git```
- ```docker run -itd -v /home/ddutt/suzieq-data/cloud-native-data-center-networking/parquet-out:/suzieq/parquet --name suzieq ddutt/suzieq:latest```
- ```docker attach suzieq```
- ```suzieq-cli```

Note that in the docker run command above, the directory name /home/ddutt/suzieq-data/... 
used assumed that the git clone of suzieq-data was done in the directory /home/ddutt. In other 
words, the host path name used in the -v option should be the **absolute path of the directory**, 
not the relative path.

From here on, you can follow the [preliminary documentation](./docs/analyzer.md) for 
further exploration. If you wish to **run the poller to gather data from your network**, 
you can do so via the instructions [here](./docs/poller.md). 

We're working on putting up more extensive documentation for every aspect of Suzieq: as 
a user, and as a contributor. We hope to be done with that by the end of this week.