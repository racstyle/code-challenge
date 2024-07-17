/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

// select the address form
const addressForm = document.querySelector('.form');

// wait for form to be submitted
addressForm.addEventListener('submit', async event => {
   event.preventDefault();    // prevent refresh

   // parse the input to be readable JSON
   const data = new FormData(addressForm);
   var dataObj = {};
   data.forEach((value, key) => dataObj[key] = value);   // this includes CSRF token, only want address input
   var parsedInput = dataObj['address'];  // extract the address input

   // try sending input to API backend
   try {
      const res = await fetch(`api/parse?address=${parsedInput}`);
      console.log(res);
   }
   catch(err) {
      console.error(err.message);
   }
});
