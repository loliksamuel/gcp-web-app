# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#gcloud projects create gcpwebbb
#gcloud config set project gcpwebbb
#gcloud app deploy


import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        print ('gettt')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello db key value simon !')
        self.response.write(' my 1st gcloud app deploy succeeded !')




app = webapp2.WSGIApplication([
    ('/'     ,	MainHandler),

     ], debug=False)


