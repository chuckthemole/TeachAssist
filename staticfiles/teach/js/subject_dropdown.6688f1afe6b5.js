var Data = {

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

let dropdown = $('#locality-dropdown');

dropdown.empty();

dropdown.append('<option selected="true" disabled>Choose State/Province</option>');
dropdown.prop('selectedIndex', 0);

//const data = 'select_list_data.json';

// Populate dropdown with list of provinces
//$.getJSON(url, function (data) {
  //$.each(Data, function (key, entry) {
    //dropdown.append($('<option></option>').attr('value', entry.abbreviation).text(entry.name));
  //})
//}
//);
