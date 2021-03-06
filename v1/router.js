/**
 * Module dependencies.
 */
const express = require('express');
/**
 * Controllers
 */
const Examples = require('./controllers/examples.controller');
const Scan = require('./controllers/scan.controller')

//Router
exports.router = (function () {
  const Router = express.Router();

  Router.route('/echo').get(Examples.show);
  Router.route('/examples/object').get(Examples.object);
  Router.route('/examples/error').get(Examples.error);
  Router.route('/examples/validator/:data').get(Examples.validator);
  Router.route('/scan').post(Scan.scan)
  Router.route('/return').get(Scan.retour)


  return Router;
})();
