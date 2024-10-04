import React, { useState } from 'react';
import axios from 'axios';

const CutCreateForm = () => {
  const [cutData, setCutData] = useState({
    cut_code: null,
    create_date: null,
    owner: null,
    sewer: null,
    model_name: null,
    model_code: null,
    lai_per_unit: null,
    product_per_layer: null,
    size: null,
    length_of_layers: null,
    cutting_price: null,
    sewing_price: null,
    cutting_price_raw: null,
    sewing_price_raw: null,
  });

  const [rolls, setRolls] = useState([
    { color: null, length: null, layers: null, products: null, type_fabric: null },
  ]);

  // Handling cut data change
  const handleCutChange = (e) => {
    setCutData({ ...cutData, [e.target.name]: e.target.value });
  };

  // Handling rolls data change
  const handleRollChange = (index, e) => {
    const updatedRolls = [...rolls];
    updatedRolls[index][e.target.name] = e.target.value;
    setRolls(updatedRolls);
  };

  // Adding a new roll
  const addRoll = () => {
    setRolls([...rolls, { color: '', length: '', layers: '', products: '', type_fabric: '' }]);
  };

  // Removing a roll
  const removeRoll = (index) => {
    const updatedRolls = rolls.filter((_, rollIndex) => rollIndex !== index);
    setRolls(updatedRolls);
  };

  // Submit the form
  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      ...cutData,
      rolls,
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/cut-create-drf/', payload, {
        headers : {
          'Content-Type': 'application/json'
        }
      });  // Adjust the endpoint accordingly
      console.log('Cut created successfully:', response.data);
    } catch (error) {
      console.error('error creating the cut:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create a new Cut</h2>
      <label>
        Cut Code:
        <input type="text" name="cut_code" value={cutData.cut_code} onChange={handleCutChange} />
      </label>

      <label>
        Create Date:
        <input type="text" name="create_date" value={cutData.create_date} onChange={handleCutChange} />
      </label>

      <label>
        Owner:
        <input type="text" name="owner" value={cutData.owner} onChange={handleCutChange} />
      </label>

      {/* Add more Cut fields here */}

      <h3>Rolls</h3>
      {rolls.map((roll, index) => (
        <div key={index}>
          <label>
            Color:
            <input type="text" name="color" value={roll.color} onChange={(e) => handleRollChange(index, e)} />
          </label>
          <label>
            Length:
            <input type="number" name="length" value={roll.length} onChange={(e) => handleRollChange(index, e)} />
          </label>
          <label>
            Layers:
            <input type="number" name="layers" value={roll.layers} onChange={(e) => handleRollChange(index, e)} />
          </label>
          <label>
            Products:
            <input type="number" name="products" value={roll.products} onChange={(e) => handleRollChange(index, e)} />
          </label>
          <label>
            Type Fabric:
            <input type="text" name="type_fabric" value={roll.type_fabric} onChange={(e) => handleRollChange(index, e)} />
          </label>

          <button type="button" onClick={() => removeRoll(index)}>Remove Roll</button>
        </div>
      ))}

      <button type="button" onClick={addRoll}>Add Roll</button>

      <button type="submit">Create Cut</button>
    </form>
  );
};

export default CutCreateForm;
