import 'package:finance_app/widgets/transaction_list.dart';
import 'package:flutter/material.dart';
import './widgets/new_transaction.dart';
import './model/transaction.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'My Expenses',
      theme: ThemeData(
          primarySwatch: Colors.lightBlue,
          accentColor: Colors.lightBlue,
          fontFamily: "Poppins",

          //this is the theme for all the text in the app
          textTheme: ThemeData.light().textTheme.copyWith(
                  titleMedium: TextStyle(
                fontFamily: "Poppins-Bold",
                fontWeight: FontWeight.normal,
                fontSize: 20,
              )),

          // this is the theme for app bar
          appBarTheme: AppBarTheme(
            backgroundColor: Color.fromARGB(99, 11, 76, 255),
            titleTextStyle: TextStyle(
                fontFamily: "Comfortaa-Regular",
                fontSize: 27,
                fontWeight: FontWeight.bold,
                color: Colors.white),
            foregroundColor: Colors.black,
          )),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override

  // String titleInput;
  final List<Transaction> _userTransactions = [
    ///TODO The part where all the transactions goes
  ];

  void _addNewTransaction(String txTitle, double txAmount) {
    final newTx = Transaction(
      title: txTitle,
      amount: txAmount,
      date: DateTime.now(),
      id: DateTime.now().toString(),
    );

    setState(() {
      _userTransactions.add(
          newTx); // The main part of the body and tran list, because of I did the setState and add (newTx) to the list of _userTransaction the newTx will be added to the list.
    });
  }

  void _startAddNewTran(BuildContext ctx) {
    showModalBottomSheet(
      context: ctx,
      builder: (_) {
        return GestureDetector(
          onTap: () => Navigator.of(context).pop(),
          child: NewTransaction(_addNewTransaction),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Color.fromARGB(219, 31, 30, 30),
        title: Text(
          'My Expenses',
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          // mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            TransactionList(_userTransactions),
          ],
        ),
      ),
      // floatingActionButtonAnimator: FloatingActionButtonAnimator.scaling,
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () => _startAddNewTran(context),
      ),
    );
  }
}
