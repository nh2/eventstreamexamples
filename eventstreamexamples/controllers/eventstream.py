# -*- coding: utf-8 -*-
"""Example controller for SSE (server-side events)"""
# adapted from http://blog.abourget.net/2010/6/16/html5-eventsource-in-pylons-read-comet-ajax-polling

import time

from tg import expose, request, response
from tg import url
from tg.decorators import with_trailing_slash

from tg import TGController

class EventstreamController(TGController):

	def load_js(self, eventurl):
		"""Page to load a JS of given URL"""
		return '<script src="%s" type="text/javascript"></script>Loaded... watch the console!' % url('eventsource_js', {'eventurl': eventurl})

	@expose(content_type='text/javascript')
	def eventsource_js(self, eventurl):
		"""Serve the JS that opens the connection and processes the events"""
		return """
document.addEventListener('DOMContentLoaded', function () {

  var eventSrc  = new EventSource('%s');

  eventSrc.addEventListener('open', function (event) {
	console.log("OPEN");
	console.log(event.type);
  });

  eventSrc.addEventListener('message', function (event) {
	console.log("RECEIVED");
	console.log(event.type);
	console.log(event.data);

  });
  console.log("Loaded...");

}, false);
""" % eventurl

	@expose()
	@with_trailing_slash
	def index(self):
		return self.load_js(url('eventstream'))

	@expose()
	def eventstream(self):
		"""SSE streaming"""
		# set content-type appropriately
		response.headers['Content-type'] = 'text/event-stream'
		# _unset_ charset because some browsers might fail otherwise
		# see http://code.google.com/p/chromium/issues/detail?id=66666 and https://bugs.webkit.org/show_bug.cgi?id=45372
		# this requires a Turbogears modification: http://groups.google.com/group/turbogears/browse_thread/thread/e1a558743f408852
		response.charset = ""
		def stream():
			for x in range(10):
				# send current iteration and time as event data
				msg = "data: %s %s\n\n" % (x, time.time())
				time.sleep(1)
				yield msg
		return stream()
