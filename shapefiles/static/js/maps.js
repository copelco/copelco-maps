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
                var marker = new google.maps.Marker({
                    'map': widget.map,
                    'title': place.name,
                    'position': new google.maps.LatLng(place.point[1], place.point[0])
                });
                widget.markers.push(marker);
                widget.bounds.extend(marker.position);
                widget._marker_added(marker);
            });
            widget.map.fitBounds(widget.bounds);
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
});
