// Use the http package: add 'http: ^0.13.3' to your pubspec.yaml file.
import 'dart:convert';

import 'package:http/http.dart' as http;

Future<void> fetchVehicleStatus() async {
  final response = await http.get(Uri.parse('http://localhost:5000/vehicle/status'));

  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body);
    print(jsonResponse);
    // Update UI with jsonResponse here
  } else {
    throw Exception('Failed to load vehicle status');
  }
}
