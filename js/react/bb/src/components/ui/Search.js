import React, { useState } from 'react';

const Search = ({ setQuery }) => {
  const [text, setText] = useState('');

  const onChange = (q) => {
    setText(q);
    setQuery(q);
  };

  return (
    <div>
      <section className="search">
        <form>
          <input
            type="text"
            className="form-control"
            placeholder="Search characters"
            val={text}
            onChange={(e) => onChange(e.target.value)}
            autoFocus
          />
        </form>
      </section>
    </div>
  );
};

export default Search;
