/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

// function to display the parsed address
function displayParsedAddr(parsedAddr) {
  console.log('%cInside display function...', "color:cyan;");
  
  var address_components = parsedAddr['address_components'];
  var input_string = parsedAddr['input_string'];
  var resultsDiv = document.getElementById('address-results');
  var errorDivPlaceholder = document.getElementById('address-error');
  
  console.log('Pulled address_components:', parsedAddr['address_components']);
  console.log('Pulled address_type:', parsedAddr['address_type']);

  // if the input is empty
  if (input_string!=null && input_string.length==0) {
    console.error('The input string is empty.');

    // if there is an existing error div, delete it to prevent element duplication
    if (errorDivPlaceholder) { errorDivPlaceholder.remove(); }

    // "parent" div to put error underneath hide results table if parsing again
    resultsDiv.style.display = 'none';

    // error div
    var errorDivNew = document.createElement('div');
    errorDivNew.innerHTML = 'Please provide a value to parse.';
    errorDivNew.setAttribute('id', 'address-error');
    errorDivNew.setAttribute('class', 'alert alert-danger');

    // add error div to HTML
    resultsDiv.parentNode.appendChild(errorDivNew);

    return;
  }
  
  // if there is an error parsing
  else if (address_components == null) {
    console.error('There is a problem with the parsed input.');
  
    // if there is an existing error div, delete it to prevent element duplication
    if (errorDivPlaceholder) { errorDivPlaceholder.remove(); }

    // "parent" div to put error underneath hide results table if parsing again
    resultsDiv.style.display = 'none';

    // error div
    var errorDivNew = document.createElement('div');
    errorDivNew.innerHTML = 'Unable to parse this value due to repeated labels. Our team has been notified of the error.';
    errorDivNew.setAttribute('id', 'address-error');
    errorDivNew.setAttribute('class', 'alert alert-danger');

    // add error div to HTML
    resultsDiv.parentNode.appendChild(errorDivNew);

    return;
  }

  // show address type
  document.getElementById('parse-type').innerText = parsedAddr['address_type'];

  // add rows to table
  var addressResultsTable = resultsDiv.getElementsByTagName('tbody')[0];  // get access to table element
  addressResultsTable.innerHTML = "";   // clear table if parsing again

  for (var address_part in address_components) {
    // create new row
    var newRow = addressResultsTable.insertRow();

    // column 1: address_part
    var addrCell = newRow.insertCell();
    var addrText = document.createTextNode(address_part);
    addrCell.appendChild(addrText);

    // column 2: tag
    var tagCell = newRow.insertCell();
    var tagText = document.createTextNode(address_components[address_part]);
    tagCell.appendChild(tagText);
  }

  // show the results div + hide the error div if present
  resultsDiv.style.display = "block";
  if (errorDivPlaceholder) { errorDivPlaceholder.remove(); }

  return;
}


// select the address form
var addressForm = document.querySelector('.form');

// wait for form to be submitted
// addressForm.addEventListener('submit', () => parseInput())
addressForm.addEventListener('submit', async function(event) {
  event.preventDefault();   // prevent refresh

  console.log('%c\n--------------- New parse session ---------------', "color:yellow;");

  // parse the input to be readable JSON
  var data = new FormData(addressForm);
  var parsedInput = data.get('address');  // get the front-end address input
  console.log('Recorded input: ' + parsedInput);

  // try sending input to API backend
  try {
    var apiURL = 'api/parse?address=' + parsedInput;

    // call the API + parse the fetched response into readable JSON and return it
    var res = await fetch(apiURL).then(function(response) {
      return response.json();
    });
    console.log('Returned parse: ', res);

    // display parsed address
    displayParsedAddr(res);
  }
  catch(err) {
    console.error('Something went wrong: ', err.message);
  }
  
  console.log('%cDone running the program.', "color:green;");
});
