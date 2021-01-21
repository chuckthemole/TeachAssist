// object literal holding data for option elements
var Select_List_Data = {

  'choices': { // name of associated select box

    // names match option values in controlling select box
    math: {
      text: ['Algebra', 'Geometry', 'Statistics', 'Calculus', 'Trigonometry'],
      value: ['algebra', 'geometry', 'statistics', 'calculus', 'trigonometry']
    },
    science: {
      text: ['Biology', 'Chemistry', 'Physics', 'Astronomy'],
      value: ['biology', 'chemistry', 'physics', 'astronomy']
    },
    english: {
      text: ['American Literature', 'World Literature', 'Creative Writing', 'Journalism'],
      value: ['biology', 'chemistry', 'physics', 'astronomy']
    },
    history: {
      text: ['Government', 'Geography', 'Ethnic Studies', 'Economics'],
      value: ['government', 'geography', 'ethnic studies', 'economics']
    }

  }
};

// removes all option elements in select box
// removeGrp (optional) boolean to remove optgroups
function removeAllOptions(sel, removeGrp) {
  var len, groups, par;
  if (removeGrp) {
    groups = sel.getElementsByTagName('optgroup');
    len = groups.length;
    for (var i = len; i; i--) {
      sel.removeChild(groups[i - 1]);
    }
  }

  len = sel.options.length;
  for (var i = len; i; i--) {
    par = sel.options[i - 1].parentNode;
    par.removeChild(sel.options[i - 1]);
  }
}

function appendDataToSelect(sel, obj) {
  var f = document.createDocumentFragment();
  var labels = [],
    group, opts;

  function addOptions(obj) {
    var f = document.createDocumentFragment();
    var o;

    for (var i = 0, len = obj.text.length; i < len; i++) {
      o = document.createElement('option');
      o.appendChild(document.createTextNode(obj.text[i]));

      if (obj.value) {
        o.value = obj.value[i];
      }

      f.appendChild(o);
    }
    return f;
  }

  if (obj.text) {
    opts = addOptions(obj);
    f.appendChild(opts);
  } else {
    for (var prop in obj) {
      if (obj.hasOwnProperty(prop)) {
        labels.push(prop);
      }
    }

    for (var i = 0, len = labels.length; i < len; i++) {
      group = document.createElement('optgroup');
      group.label = labels[i];
      f.appendChild(group);
      opts = addOptions(obj[labels[i]]);
      group.appendChild(opts);
    }
  }
  sel.appendChild(f);
}

function addClass() {
  var select = document.getElementById('choices');
  var opt = document.createElement('option');
  add_class = document.getElementById("add_class").value;
  opt.value = add_class;
  opt.innerHTML = add_class;
  select.appendChild(opt);
}

function addSubject() {

}

// anonymous function assigned to onchange event of controlling select box
document.forms['create_lesson'].elements['subject'].onchange = function(e) {
  // name of associated select box
  var relName = 'choices';

  // reference to associated select box
  var relList = this.form.elements[relName];

  // get data from object literal based on selection in controlling select box (this.value)
  var obj = Select_List_Data[relName][this.value];

  // remove current option elements
  removeAllOptions(relList, true);

  // call function to add optgroup/option elements
  // pass reference to associated select box and data for new options
  appendDataToSelect(relList, obj);
};

// populate associated select box as page loads
(function() { // immediate function to avoid globals

  var form = document.forms['create_lesson'];

  // reference to controlling select box
  var sel = form.elements['subject'];
  sel.selectedIndex = 0;

  // name of associated select box
  var relName = 'choices';
  // reference to associated select box
  var rel = form.elements[relName];

  // get data for associated select box passing its name
  // and value of selected in controlling select box
  var data = Select_List_Data[relName][sel.value];

  // add options to associated select box
  appendDataToSelect(rel, data);

}());
