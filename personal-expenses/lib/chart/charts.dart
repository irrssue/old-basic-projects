import 'dart:ffi';

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:syncfusion_flutter_charts/charts.dart';
import '../model/transaction.dart';
import 'package:intl/intl.dart';


class Chart extends StatelessWidget {

  final List<Transaction> recentTransactions;

  Chart(this.recentTransactions);

  List<Map<String, Object>> get groupTransactionValues {
    return List.generate(7, (index){
      final weekDay = DateTime.now().subtract(Duration(days: index),);

      var totalSum = 0.0;

      for (var total = 0; total < recentTransactions.length; total++) {
        if (recentTransactions[total].date.day == weekDay.day && recentTransactions[total].date.month == weekDay.month && 
        recentTransactions[total].date.year == weekDay.year) {
          totalSum += recentTransactions[total].amount;
        }
      }

      return {
        "Day": DateFormat.E(weekDay), 
        "amount": totalSum
      };
    });
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: SfCartesianChart(),
      ),
    );
  }

  List<Chart> getChartData(){
    final List<Chart> chartData = [
      
    ]
  }

}

// class GDPData {
//   GDPData(this.continent, this.gdp);
//   final String continent;
//   final int gdp;
// }
