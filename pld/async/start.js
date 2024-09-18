endPoint = 'https://jsonplaceholder.typicode.com/users';

const testAsync = async () => {
    response = await fetch(`${endPoint}/1`);
    data = await response.json()
    console.log(data.id);
    newResponse = await fetch(`${endPoint}/2`);
    secData = await newResponse.json();
    console.log(secData.id);
}

testAsync();