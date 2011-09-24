/**
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Library General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 *
 * The Product Search Results table.
 * Copyright (C) 2011 Simon Newton
 */

goog.require('goog.dom');
goog.require('goog.events');
goog.require('goog.ui.Component');
goog.require('goog.ui.TableSorter');


goog.provide('app.ModelTable');


/**
 * Create a new product table object.
 * @constructor
 */
app.ModelTable = function(element, state_manager) {
  var table = new goog.ui.TableSorter();
  table.decorate(goog.dom.$(element));
  table.setSortFunction(0, goog.ui.TableSorter.alphaSort);
  table.setSortFunction(1, goog.ui.TableSorter.numericSort);
  table.setSortFunction(2, goog.ui.TableSorter.alphaSort);

  this.result_rows = new app.ResultsRows(state_manager);

  var table = goog.dom.$(element);
  var tbody = table.getElementsByTagName(goog.dom.TagName.TBODY)[0];
  this.result_rows.decorate(tbody);
};


/**
 * Update the product table with new data.
 */
app.ModelTable.prototype.update = function(new_models) {
  this.result_rows.removeChildren(true);

  for (var i = 0; i < new_models.length; ++i) {
    var model = new_models[i];
    var new_row = new app.ModelRow(model, this._state_manager);
    this.result_rows.addChild(new_row, true);
  }
};


/**
 * A row in the device model results table.
 * @constructor
 */
app.ModelRow = function(pid, state_manager, opt_domHelper) {
  goog.ui.Component.call(this, opt_domHelper);
  this._pid = pid;
  this._state_manager = state_manager;
};
goog.inherits(app.ModelRow, goog.ui.Component);


/**
 * Return the underlying pid
 */
app.ModelRow.prototype.pid = function() { return this._pid; };


/**
 * This component can't be used to decorate
 */
app.ModelRow.prototype.canDecorate = function() { return false; };


/**
 * Create the dom for this component
 */
app.ModelRow.prototype.createDom = function() {
  var tr = this.dom_.createDom(
      'tr', {},
      goog.dom.createDom('td', {}, this._pid['manufacturer_name']),
      goog.dom.createDom('td',
                         {},
                         '0x' + app.toHex(this._pid['device_model_id'], 4)),
      goog.dom.createDom('td', {}, this._pid['model_description']));
  this.setElementInternal(tr);
};


/**
 * Attach the event handler
 */
app.ModelRow.prototype.enterDocument = function() {
  app.ModelRow.superClass_.enterDocument.call(this);
  // TODO(simon): add this later
  /*
  goog.events.listen(
    this.getElement(),
    goog.events.EventType.CLICK,
    this._rowClicked,
    false,
    this);
  */
};


/**
 * Remove the event hanler
 */
app.ModelRow.prototype.exitDocument = function() {
  app.ModelRow.superClass_.exitDocument.call(this);
  /*
  goog.events.unlisten(
    this.getElement(),
    goog.events.EventType.CLICK,
    this._rowClicked,
    false,
    this);
  */
};


/**
 * Call when the user clicks on this row
 */
app.ModelRow.prototype._rowClicked = function() {
  this._state_manager.displayModel(this._pid['manufacturer_id'],
                                   this._pid['device_model_id']);
};
