$.widget("ui.map", {
    options: {
        'map-options': {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        }
    },
    _create: function() {
        var widget = this;
        widget._init_map();
        widget._init_window();
        widget._load_markers();
    },
    _init_map: function() {
        var widget = this;
        widget.markers = [];
        widget.bounds = new google.maps.LatLngBounds();
        widget.map = new google.maps.Map(widget.element[0], widget.options['map-options']);
    },
    _init_window: function() {
        var widget = this;
        widget.window = new google.maps.InfoWindow({
            'size': new google.maps.Size(150, 50)
        });
        google.maps.event.addListener(widget.map, 'click', function() {
            widget.window.close();
        });
    },
    _load_markers: function() {
        var widget = this;
        $.getJSON(widget.options['markers'], function(data) {
            $.each(data.objects, function(idx, place) {
                widget.add_marker({'title': place.name, 'point': place.point});
            });
            widget.fit_bounds();
        });
    },
    _marker_added: function(marker) {
        var widget = this;
        google.maps.event.addListener(marker, 'click', function(event) {
            widget.window.setPosition(marker.position);
            widget.window.setContent(marker.title);
            widget.window.open(widget.map);
        });
    },
    add_marker: function(data) {
        var widget = this;
        var marker = new google.maps.Marker({
            'map': widget.map,
            'title': data.title,
            'position': new google.maps.LatLng(data.point[1], data.point[0])
        });
        widget.markers.push(marker);
        widget.bounds.extend(marker.position);
        widget._marker_added(marker);
    },
    fit_bounds: function() {
        var widget = this;
        widget.map.fitBounds(widget.bounds);
    },
    zoom: function(zoom) {
        var widget = this;
        widget.map.setZoom(zoom);
    },
    center: function(point) {
        var widget = this;
        widget.map.setCenter(new google.maps.LatLng(point[1], point[0]));
    }
});
