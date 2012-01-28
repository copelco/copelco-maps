$.widget("ui.map", {
    options: {
        'map-options': {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        }
    },
    _create: function() {
        var widget = this;
        widget.markers = [];
        widget.bounds = new google.maps.LatLngBounds();
        var map = new google.maps.Map(widget.element[0], widget.options['map-options']);
        var info_window = new google.maps.InfoWindow({ 
            'size': new google.maps.Size(150, 50)
        });
        google.maps.event.addListener(map, 'click', function() {
            info_window.close();
        });
        $.getJSON(widget.options['url'], function(data) {
            $.each(data.objects, function(idx, place) {
                var marker = new google.maps.Marker({
                    'map': map,
                    'title': place.name,
                    'position': new google.maps.LatLng(place.point[1], place.point[0])
                });
                widget.markers.push(marker);
                widget.bounds.extend(marker.position);
                google.maps.event.addListener(marker, 'click', function(event) {
                    info_window.setPosition(marker.position);
                    info_window.setContent(place.name);
                    info_window.open(map);
                });
            });
            map.fitBounds(widget.bounds);
        });
    },
});
