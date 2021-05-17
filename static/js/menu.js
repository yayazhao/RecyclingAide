(function( prime, $, kendo, undefined) {

    prime.openMenu = function() {
        prime.menu_container.stop().animate({'marginLeft':'-2px'}, 200);
    }

    prime.closeMenu = function() {
        prime.menu_container.stop().animate({'marginLeft':'-223px'}, 200);
    }

    prime.pinMenu = function() {
        var main = $("#main");
        main.css('marginLeft':'-220px');
        prime.menuPin.removeClass('s-icon-unpinned').addClass('s-icon-pinned');
        prime.menuPin.attr('title', 'unpin menu');
        prime.globalViewModel.set('menuPinned', true));
        $.cookie('menuStatus', 'pinned', { path: '/', expires:999});
    }

    prime.unpinMenu = function() {
        var main = $("#main");
        main.css('marginLeft':'0px');
        prime.menuPin.removeClass('s-icon-pinned').addClass('s-icon-unpinned');
        prime.menuPin.attr('title', 'pin menu');
        prime.globalViewModel.set('menuPinned', false));
        $.cookie('menuStatus', 'unpinned', { path: '/', expires:999});
    }

} (window.prime = window.prime || {}, jQuery, kendo));

$(function() {

    prime.menu_container = $('#menu_container');
    prime.menu = $('#floating_menu');
    if (prime.globalViewModel.get('showMenu')===true) {
        prime.menu.kendoTreeView({
            dataSource: [
                {'Title': 'Home', 'Url': '/'},
                {'Title': 'Facility List', 'Url': '/facility_list'},
                {'Title': 'Facility Map', 'Url': '/facility_map'}
            ],
            dataTextField: "Title",
            dataUrlField: "Url"
        });
        prime.menu_container.hover(
            function () {
                prime.openMenu();
            },
            function () {
                if (!prime.globalViewModel.get('menuPinned')) {
                    prime.closeMenu();
                }
            }
        )
    } else {
        prime.menu_container.hide();
    }

    prime.menuPin = $('menu_pin').click(function() {
        if (!prime.globalViewModel.get('menuPinned')) {
            prime.pinMenu();
        } else {
            prime.unpinMenu();
        }
    });

    prime.menuClose = $('menu_close').click(function() {
        prime.unpinMenu();
        prime.closeMenu();
    });

    if ($.cookie('menuStatus') === 'pinned') {
        prime.pinMenu();
        prime.openMenu();
    } else {
        prime.unpinMenu();
    }


});

// ---------------------------------------------------------------------------

var map;

function initialize() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: new google.maps.LatLng(46.3485167, 21.9843998),
    scrollwheel: true,
    disableDefaultUI: true,
    mapTypeId: 'roadmap',
    styles: [{
      "featureType": "road.highway",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "road.arterial",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "road.local",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "administrative.locality",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "poi",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "landscape.natural",
      "stylers": [{
        "visibility": "on"
      }, {
        "color": "#808080"
      }, {
        "lightness": 96
      }]
    }, {
      "featureType": "landscape.natural",
      "elementType": "geometry.stroke",
      "stylers": [{
        "visibility": "off"
      }]
    }, {}]
  });
  var iconBase = 'http://www.loading-systems.com/sites/default/files/images/website2016/';
  var icons = {
    office: {
      name: 'Offices',
      icon: iconBase + 'map-marker-office.png'
    },
    factory: {
      name: 'Factory',
      icon: iconBase + 'map-marker-factory.png'
    },
    dealer: {
      name: 'Distributor',
      icon: iconBase + 'map-marker-dealer.png'
    }
  };

  function addMarker(feature) {
    var marker = new google.maps.Marker({
      position: feature.position,
      icon: icons[feature.type].icon,
      map: map
    });
  }

  function addOption(feature, i) {
    var name = 'marker ' + i; // you should have the name of the location in the data
    var option = '<option value="' + i + '">' + name + '</option>';
    document.getElementById('dropdown').innerHTML += option;
  }

  function selectOpion(selectElm) {
    var i = Number(selectElm.value);
    map.setCenter(features[i].position);
    map.setZoom(6); // with many markers per country you could zoom/pan with the boundaries ...
  }
  // onChange of the select element
  google.maps.event.addDomListener(document.getElementById('dropdown'), 'change', function(e) {
    selectOpion(this);
  });
  var features = [{
    position: new google.maps.LatLng(52.4997173, 5.4302006),
    type: 'office'
  }, {
    position: new google.maps.LatLng(51.2368042, 4.4566387),
    type: 'office'
  }, {
    position: new google.maps.LatLng(50.1152834, 8.5038213),
    type: 'office'
  }, {
    position: new google.maps.LatLng(53.6245002, -1.7210977),
    type: 'office'
  }, {
    position: new google.maps.LatLng(49.0383945, 2.6853833),
    type: 'office'
  }, {
    position: new google.maps.LatLng(52.4260763, 16.8591883),
    type: 'office'
  }, {
    position: new google.maps.LatLng(50.0033534, 14.4028093),
    type: 'office'
  }, {
    position: new google.maps.LatLng(48.6130105, 17.7152123),
    type: 'office'
  }, {
    position: new google.maps.LatLng(24.8875455, 55.1403156),
    type: 'office'
  }, {
    position: new google.maps.LatLng(59.8841107, 30.3249023),
    type: 'office'
  }, {
    position: new google.maps.LatLng(47.05361, 21.9299127),
    type: 'office'
  }];

  for (var i = 0, feature; feature = features[i]; i++) {
    addMarker(feature);
    addOption(feature, i);
  }

}



