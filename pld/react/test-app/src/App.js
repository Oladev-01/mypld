import React, { useState } from "react";

const App = () => {
  const [count, setCount] = useState(0)

  return (
    <div>
      <h1>testing useState</h1>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
export default App;
