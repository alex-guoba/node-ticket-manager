###
# test for api
###

## Module dependencies
should = require "should"
request = require "request"

HOST = "http://localhost:3456"

TIMESTAMP = Date.now()

## Test cases
describe "test api", ->

  before () ->
    # before test happen

  describe "/api/tickets/new", ->
    path = "/api/tickets/new"

    it "should create ticket", (done) ->
      title = "title of ticket #{TIMESTAMP}"
      owner = "admin"
      options =
        method: 'POST'
        url: "#{HOST}#{path}"
        json :
          title : title
          owner_id : owner
          category : "test api"
          content :
            detailed : "content of ticket",
            mixed : ["data"]

      request options, (err, res, body)->
        #console.log "[api_test] \n\t\terr:%j \n\t\tres:%j \n\t\tbody:%j", err, res, body

        should.not.exist err
        should.exist res
        res.statusCode.should.eql 200
        should.exist body
        body.title.should.eql title
        body.owner_id.should.eql owner
        done()


    it "fail to create duplicate ticket", (done) ->
      title = "title of ticket #{TIMESTAMP}"
      owner = "admin"
      options =
        method: 'POST'
        url: "#{HOST}#{path}"
        json :
          title : title
          owner_id : owner
          category : "test api"
          content :
            detailed : "content of ticket",
            mixed : ["data"]

      request options, (err, res, body)->
        console.log "[api_test] \n\t\terr:%j \n\t\tres:%j \n\t\tbody:%j", err, res.statusCode, body

        should.not.exist err
        should.exist res
        res.statusCode.should.not.eql 200
        done()

  describe "/api/tickets/assign", ->
    path = "/api/tickets/assign"
    it "assign ticket to worker", (done)->
      options =
        method: 'PUT'
        url: "#{HOST}#{path}"
        json :
          worker : "test worker"
          category : "test api"

      request options, (err, res, body)->
        console.log "[api_test] \n\t\terr:%j \n\t\tres:%j \n\t\tbody:%j", err, res.statusCode, body

        should.not.exist err
        should.exist res
        res.statusCode.should.eql 200
        done()

    # here: TODO: hold the ticket in memory, comment it and compelte it














