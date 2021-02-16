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
      value: ['American Literature', 'World Literature', 'Creative Writing', 'Journalism']
    },
    history: {
      text: ['Government', 'Geography', 'Ethnic Studies', 'Economics'],
      value: ['government', 'geography', 'ethnic studies', 'economics']
    }

  }
};

export { Select_List_Data };
