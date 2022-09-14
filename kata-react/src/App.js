import { Component} from "react";

import {Card, Container, Row, Col, Button, Form} from "react-bootstrap"
import "bootstrap/dist/css/bootstrap.min.css"

class App extends Component{
  
  constructor(props){
    super(props);
     
    this.state = {
      item: {},
      isLoaded: false
    }
  }

  componentDidMount(){
    fetch("http://0.0.0.0:8080/api/v1/status")
    .then(res => res.json())
    .then(json => {
      this.setState({
        isLoaded: true,
        item: json
      })

    });
  }
  async wrapKata(){
    
    let content = document.getElementById("text2wrap").value;
    let col = document.getElementById("col4wrap").value;
    
    try{
      fetch("http://0.0.0.0:8080/api/v1/kata", {
        method: "post",
        mode: "cors",
        headers:{
          "Accept": "application/json",
          "Content-type": "application/json"
        },
        body: JSON.stringify({
          "content": content,
          "len": col
        })

      }).then(response => response.json().then(data => ({
        data: data,
        status: response.status
      })
      )).then(res => {
        
        document.getElementById("result").innerHTML = res.data.result;
      });
      
      
    }
    catch(e){
      console.log(e);
    }
  }
  render() {
    
    var {isLoaded, item} = this.state;
    if (!isLoaded){
      return (
        <div>Loading..</div>
      )
    }
    else{
      
      return (
        <>
        <div className="App">
          <header className="App-header">
            <Container>
            <div><h4>{item}</h4></div>
            <Form>
              <Row>
                <Col>
                <Form.Group>
            
            <Form.Control as="textarea" id="text2wrap" rows="10" placeholder="write your text here"></Form.Control>
          </Form.Group>
          </Col>
                <Col>
                <Form.Group>
            
            <Form.Control as="textarea" id="result" rows="10" placeholder="result will appear here" disabled={true}></Form.Control>
          </Form.Group>
                </Col>
              </Row>
              
              </Form>
              <Card>
      
      <Card.Body>
      <Card.Title>write number here</Card.Title>
      <input id="col4wrap" type="number" step="1" min="0"></input>
        <Card.Title></Card.Title>
        
        <Button variant="primary" onClick={()=>this.wrapKata()}>Wrap Text</Button>
        
      </Card.Body>
    </Card>
        
      
      
      </Container>
      </header>
      </div>
      </>
      );
    }
    
  }
}

export default App;
