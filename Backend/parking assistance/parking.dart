import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:http/http.dart' as http;

class ParkingMapScreen extends StatefulWidget {
  @override
  _ParkingMapScreenState createState() => _ParkingMapScreenState();
}

class _ParkingMapScreenState extends State<ParkingMapScreen> {
  GoogleMapController _mapController;
  Set<Marker> _markers = {};

  void _onMapCreated(GoogleMapController controller) {
    _mapController = controller;
  }

  Future<void> findParking(String location) async {
    final response = await http.get(Uri.parse('http://localhost:5000/find_parking?location=$location'));

    if (response.statusCode == 200) {
      var data = jsonDecode(response.body);
      List places = data['results'];
      setState(() {
        _markers.clear();
        for (var place in places) {
          _markers.add(Marker(
            markerId: MarkerId(place['id']),
            position: LatLng(place['geometry']['location']['lat'], place['geometry']['location']['lng']),
            infoWindow: InfoWindow(title: place['name']),
          ));
        }
      });
    } else {
      throw Exception('Failed to load parking spots');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: GoogleMap(
        onMapCreated: _onMapCreated,
        initialCameraPosition: CameraPosition(
          target: LatLng(11.9416, 79.8083),  // Example initial position: Pondicherry
          zoom: 14.0,
        ),
        markers: _markers,
      ),
    );
  }
}
