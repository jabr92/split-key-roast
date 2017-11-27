"""Calls related to roasting."""
from . import core
from .. import mongo
from ..libs.utils import paranoid_clean
from bson.objectid import ObjectId
from flask import current_app as app
from flask import render_template, jsonify
from flask_login import login_required, current_user


@core.route('/roast')
@login_required
def active_roast():
    """Render the roast page."""
    c = mongo.db[app.config['INVENTORY_COLLECTION']]
    items = c.find({'user': current_user.get_id()})
    output = list()
    for x in items:
        x['id'] = str(x['_id'])
        output.append(x)
    output.sort(key=lambda x: x['datetime'], reverse=True)
    return render_template('roast.html', inventory=output)


@core.route('/roast/<roast_id>')
@login_required
def historic_roast(roast_id):
    """Render a previous roast page."""
    # Collect the roast history data
    c = mongo.db[app.config['HISTORY_COLLECTION']]
    roast_id = paranoid_clean(roast_id)
    item = c.find_one({'_id': ObjectId(roast_id)})
    if not item:
        return jsonify({'success': False, 'message': 'No such roast.'})
    item['id'] = str(item['_id'])
    derived = {'s1': list(), 's2': list(), 's3': list(), 's4': list(),
               'flags': list()}
    for p in item['events']:
        if 'event' in p:
            label = "%s (%d, %d)" % (p['event'],
                                     int(p['config']['environment_temp']),
                                     int(p['config']['bean_temp']))
            derived['flags'].append({'x': p['time'], 'title': str(label)})
            continue
        derived['s1'].append([p['time'], p['config']['environment_temp']])
        derived['s2'].append([p['time'], p['config']['bean_temp']])
        derived['s3'].append([p['time'], p['config']['main_fan'] * 10])
        derived['s4'].append([p['time'], p['config']['heater']])

    # Collect the inventory data
    c = mongo.db[app.config['INVENTORY_COLLECTION']]
    items = c.find({'user': current_user.get_id()})
    inventory = list()
    for x in items:
        x['id'] = str(x['_id'])
        inventory.append(x)
    inventory.sort(key=lambda x: x['datetime'], reverse=True)

    # Collect the cupping data
    cuppings = list()

    return render_template('historic_roast.html', roast=item,
                           inventory=inventory, derived=derived,
                           cuppings=cuppings)
