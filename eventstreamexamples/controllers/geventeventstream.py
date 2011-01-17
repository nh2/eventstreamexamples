# -*- coding: utf-8 -*-
"""
Example controller for SSE (server-side events) with gevent.
Builds on the simple SSE controller.
"""

import sys
import time

import gevent.queue

from tg import expose, request, response
from tg import url
from tg.decorators import with_trailing_slash

from eventstream import EventstreamController

class GeventEventstreamController(EventstreamController):

	# set containing a gevent queue for each of the clients (browsers) listening for events
	client_queues = set()

	@expose()
	@with_trailing_slash
	def index(self):
		"""whenever a new client opens this page, sends an event to all listening clients"""
		# put a gevent event in each client's queue
		for q in GeventEventstreamController.client_queues:
			q.put("visit received from %(REMOTE_ADDR)s with user agent %(HTTP_USER_AGENT)s" % request.environ)
		# return the page for listening
		return self.load_js(url('visitstream'))

	@expose()
	def visitstream(self):
		"""sends a SSE whenever somebody visits index"""
		# set charset appropriately
		response.headers['Content-type'] = 'text/event-stream'
		# disable charset (see EventstreamController)
		response.charset = ""

		# create a new queue for this new listening client
		q = gevent.queue.Queue()
		GeventEventstreamController.client_queues.add(q)

		def stream():
			while True:
				yield "data: %s %s\n\n" % (q.get(), time.time())

		return stream()
