import 'dart:convert';

import 'package:http/http.dart' as http;

Future<void> manageEnergySharing(int energyToShare) async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/manage-energy'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, dynamic>{'energy_to_share': energyToShare}),
  );

  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body);
    print(jsonResponse['message']);
  } else {
    throw Exception('Failed to manage energy sharing.');
  }
}

Future<int> getBatteryStatus() async {
  final response =
      await http.get(Uri.parse('http://localhost:5000/manage-energy'));

  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body);
    return jsonResponse['battery_level'];
  } else {
    throw Exception('Failed to get battery status.');
  }
}
