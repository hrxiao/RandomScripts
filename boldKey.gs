/*
Bold the key of each definition
A key is any phrase that is followed by the string ' - '
Goes through each paragraph (line) and search for the string and set the key to bold
*/
function boldKey() {
  var body = DocumentApp.getActiveDocument().getBody();
  var numParas = body.getNumChildren();
  for (var i = 0; i < numParas; ++i) {
    var element = body.getChild(i).findText('.* - ');
    if (element != null && element.isPartial()) {
      var text = element.getElement().editAsText();
      var start = element.getStartOffset();
      var finish = element.getEndOffsetInclusive() - 3; 
      text.setBold(start, finish, true);
    }
  }
  /* ----- This does not work since it treats the whole document as one element
  var element = body.findText('.* - ');
  if (element != null) {
    var text = element.getElement().editAsText();
    var start = element.getStartOffset();
    var finish = element.getEndOffsetInclusive() - 3; 
    text.setBold(start, finish, true);
    element = body.findText('.* - ', element);
  }
  */
}

function onOpen() {
  DocumentApp.getUi().createMenu('Scripts')
      .addItem('Bold Key', 'boldKey')
      .addToUi();
}
