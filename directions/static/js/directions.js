$.widget("ui.directions", $.ui.map, {
    _create: function() {
        var widget = this;
        $.ui.map.prototype._create.call(this);
        widget.direction_service = new google.maps.DirectionsService();
        widget.direction_renderer = new google.maps.DirectionsRenderer();
        widget.direction_renderer.setMap(widget.map)
    },
    _marker_added: function(marker) {
        var widget = this;
        if (marker.title == 'Hotel') {
            widget.home = marker;
            return;
        }
        google.maps.event.addListener(marker, 'click', function(event) {
            var request = {
                origin: widget.home.position,
                destination: marker.position,
                travelMode: google.maps.DirectionsTravelMode.DRIVING
            };
            widget.direction_service.route(request, function(response, status) {
                if (status == google.maps.DirectionsStatus.OK) {
                    widget.direction_renderer.setDirections(response);
                    var leg = response.routes[0].legs[0];
                    console.log(leg);
                    var content = marker.title;
                    content += "<br />" + leg.distance.text + " - " + leg.duration.text;
                    widget.window.setPosition(marker.position);
                    widget.window.setContent(content);
                    widget.window.open(widget.map);
                } else {
                    alert("Directions response " + status);
                }
            });
        });
    }
});
