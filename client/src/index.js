import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

import { 
  ApolloClient, 
  InMemoryCache,
  ApolloLink,
  HttpLink,
  ApolloProvider,
} from '@apollo/client'

import { setContext } from '@apollo/client/link/context';

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const httpLink = new HttpLink({ uri: 'http://localhost:8000/api/graphql' });

const authLink = setContext((_, { headers }) => {
  return {
    headers: {
      ...headers,
      'X-CSRFToken': csrftoken ? csrftoken : "",
    }
  }
});

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache()
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>
  </React.StrictMode>
);
