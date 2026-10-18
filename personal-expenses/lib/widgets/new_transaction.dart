import 'package:flutter/material.dart';

class NewTransaction extends StatefulWidget {
  final Function addnewtran;

  NewTransaction(this.addnewtran);

  @override
  State<NewTransaction> createState() => _NewTransactionState();
}

class _NewTransactionState extends State<NewTransaction> {
  final titleController = TextEditingController();

  final amountController = TextEditingController();

  void submitdata() {
    //TODOI put dynamic here

    final enterTitle = titleController.text;
    final enterAmount = double.parse(amountController.text);

    if (enterTitle.isEmpty || enterAmount <= 0) {
      return; //if I just leave return like this code after that or under that will not be reacheable meanning: the code will not be excitude
    }

    widget.addnewtran(
      enterTitle,
      enterAmount,
    );

    Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 5,
      child: Container(
        padding: EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            TextField(
              decoration: InputDecoration(labelText: 'Title'),
              controller: titleController,
              // onChanged: (val) {
              //   titleInput = val;
              // },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Amount'),
              controller: amountController,
              onSubmitted: (_) => submitdata,
              // onChanged: (val) {
              //   amountInput = val;
              // },
            ),
            FlatButton(
              child: Text('Add Transaction'),
              textColor: Color.fromARGB(255, 0, 0, 0),
              onPressed: submitdata,
            ),
          ],
        ),
      ),
    );
  }
}
