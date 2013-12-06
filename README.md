skyscrapepy
===========

Python Library to be used with the Skyscraper scraping metaframework https://github.com/opendatacity/skyscraper


## Installation

````
python setup.py install
````

## Usage

The skyscraper client can be used as a context guard with python's with statement, see below. 
 
Start of the with block will send the start message. Any exception raised during execution of the code within the with block will be reported as an error. End of the with block will send an end message. 

The context guard can send messages to the skyscraper infrastructure to signal progress, success,
failure or plain existence.

## Messages 

* `start` execution has begun.
* `end` execution has ended.
* `ping` scraper still executed and has not yet broken apart.
* `success` scraper has achieved a portion of a quest successfully.
* `warn` scraper ran into troubles which may be worth looking upon.
* `error` scraper has broken down and requires immediate attention.
* `log` scraper wants something to be written down for a later look upon.


## Example Usage

```` python 

from skyscraper.client import Client
import time

sclient=Client()

with sclient.create("Time is up",
		    run_timer=10,
		    contacts=[dict(email="skyscraper-timeup@mailinator.com",name="Martin Virtel")]) as jobwatcher :
	time.sleep(20)
	#
	# Alert will be sent after 10 seconds
	#
	jobwatcher.ping()
	jobwatcher.log("I pinged!")


with sclient.create("Exception happened",
		    run_timer=100,
		    contacts=[dict(email="skyscraper-timeup@mailinator.com",name="Martin Virtel")]) as jobwatcher :
	a=10/0
	#
	# Division by 0 will be reported
	#



````

## Parameters for the create method

These are conditions and threshold for alerts to be triggered. There are `timer` and `counter` hooks. Timer hooks get triggered on exceeded time limits, couter hooks on exceeded or missed number of counts.

* `start_timer` The maximum time between two `start` signals
* `run_timer` The maximum time between `start` and `end` signals
* `ping_timer` The maximum time between two `ping` signals
* `success_timer` The maximum time between two `success` signals
* `warning_counter_max` The maximum number of warning signals during one execution
* `success_counter_min` The minimum number of success signals during one execution
* `success_counter_max` The maximum number of success signals during one execution
* `ping_counter_min` The minimum number of ping signals during one execution
* `ping_counter_max` The maximum number of ping signals during one execution


