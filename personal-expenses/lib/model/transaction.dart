import 'package:flutter/foundation.dart';

class Transaction {
  String id; // the id number of the card
  String title; // the title of the card i.e name
  double amount; // the amounts of the acrd i.e $
  DateTime date; // the date and time of the card

  Transaction({
    required this.id,
    required this.title,
    required this.amount,
    required this.date,
  });
}
