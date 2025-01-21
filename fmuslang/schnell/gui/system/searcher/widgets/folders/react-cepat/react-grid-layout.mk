--% default
import React, {useState} from "react";
import { EmbeddedTweet, Tweet } from "react-tweet";
import { Timeline, Tweet as RTweet } from "react-twitter-widgets";
import "./App.css";
import GridLayout from "react-grid-layout";
import styled from "styled-components";

// import React from 'react';
import { Responsive, WidthProvider } from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';
import 'react-resizable/css/styles.css';

const ResponsiveGridLayout = WidthProvider(Responsive);


const small = 1;
const big = 2;
const NewspaperLayout = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const handleCollapse = () => {
    setIsCollapsed(!isCollapsed);
  };

  // Define the grid layout configuration
  const layout = [
    { i: 'item0', x: 0, y: 0, w: isCollapsed ? small : big, h: 10, color: '#F08080', content: 'Collapsible Item' },
    { i: 'item1', x: isCollapsed ? small : 2, y: 0, w: isCollapsed ? 3 : 2, h: 2, color: '#FF0000', content: 'Article 1' },
    { i: 'item2', x: isCollapsed ? small+1 : 4, y: 0, w: 2, h: 4, color: '#00FF00', content: 'Article 2' },
    { i: 'item3', x: isCollapsed ? small+1 : 6, y: 0, w: 1, h: 2, color: '#0000FF', content: 'Article 3' },
    { i: 'item4', x: isCollapsed ? small+1 : 2, y: 2, w: 2, h: 2, color: '#FFA500', content: 'Article 4' },
    { i: 'item5', x: isCollapsed ? small+1 : 4, y: 2, w: 2, h: 3, color: '#800080', content: 'Article 5' },
    { i: 'item6', x: isCollapsed ? small+1 : 6, y: 2, w: 1, h: 2, color: '#FFFF00', content: 'Article 6' },
    { i: 'item7', x: isCollapsed ? small+1 : 2, y: 4, w: 2, h: 3, color: '#008000', content: 'Article 7' },
    { i: 'item8', x: isCollapsed ? small+1 : 4, y: 5, w: 2, h: 2, color: '#FFC0CB', content: 'Article 8' },
    { i: 'item9', x: isCollapsed ? small+1 : 6, y: 4, w: 1, h: 2, color: '#000000', content: 'Article 9' },
    { i: 'item10', x: 0, y: 7, w: 6, h: 3, color: '#808080', content: 'Static Article at Bottom', isDraggable: false, isResizable: false },
  ];

  return (
    <GridLayout className="layout" layout={layout} cols={6} rowHeight={100} width={1200}>
      {layout.map((item) => (
        <div key={item.i} style={{ backgroundColor: item.color }}>
          {item.i === 'item0' && (
            <div>
              {isCollapsed ? (
                <button onClick={handleCollapse}>Expand</button>
              ) : (
                <div>
                  <button onClick={handleCollapse}>Collapse</button>
                  {item.content}
                </div>
              )}
            </div>
          )}
          {item.i !== 'item0' && item.content}
        </div>
      ))}
    </GridLayout>
  );
};

export default NewspaperLayout;
--#

--% template
import React, {useState} from "react";
import { EmbeddedTweet, Tweet } from "react-tweet";
import { Timeline, Tweet as RTweet } from "react-twitter-widgets";
import GridLayout from "react-grid-layout";
import styled from "styled-components";
import { Responsive, WidthProvider } from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';
import 'react-resizable/css/styles.css';

import "./App.css";

const ResponsiveGridLayout = WidthProvider(Responsive);

const NewspaperLayout = () => {
  const layout = [
    { i: 'item1', x: 0, y: 0, w: 2, h: 2, color: '#FF0000', content: 'Article 1' },
    { i: 'item2', x: 2, y: 0, w: 2, h: 4, color: '#00FF00', content: 'Article 2' },
    { i: 'item3', x: 4, y: 0, w: 1, h: 2, color: '#0000FF', content: 'Article 3' },
    { i: 'item4', x: 0, y: 2, w: 2, h: 2, color: '#FFA500', content: 'Article 4' },
    { i: 'item5', x: 2, y: 2, w: 2, h: 3, color: '#800080', content: 'Article 5' },
    { i: 'item6', x: 4, y: 2, w: 1, h: 2, color: '#FFFF00', content: 'Article 6' },
    { i: 'item7', x: 0, y: 4, w: 2, h: 3, color: '#008000', content: 'Article 7' },
    { i: 'item8', x: 2, y: 5, w: 2, h: 2, color: '#FFC0CB', content: 'Article 8' },
    { i: 'item9', x: 4, y: 4, w: 1, h: 2, color: '#000000', content: 'Article 9' },
    { i: 'item10', x: 0, y: 7, w: 6, h: 3, color: '#808080', content: 'Static Article at Bottom', isDraggable: false, isResizable: false  },
  ];

  return (
    <GridLayout className="layout" layout={layout} cols={6} rowHeight={100} width={1200}>
      {layout.map((item) => (
        <div key={item.i} style={{ backgroundColor: item.color }}>
          {item.content}
        </div>
      ))}
    </GridLayout>
  );
}

export default NewspaperLayout;
--#

--% fmuslang
C:\hapus\ngetweet\,d
  /ketik)ps
--#

--% rujukan
<ResponsiveGridLayout
  className="layout"
  breakpoints={{ lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }}
  cols={{ lg: 10, md: 8, sm: 6, xs: 4, xxs: 2 }}
  rowHeight={100}
  margin={[16, 16]}
  containerPadding={[16, 16]}
>

</ResponsiveGridLayout>

ini perlu nih:
cols={{ lg: 10, md: 8, sm: 6, xs: 4, xxs: 2 }}
--#

--% sample/2
import React, {useState} from "react";
import { EmbeddedTweet, Tweet } from "react-tweet";
import { Timeline, Tweet as RTweet } from "react-twitter-widgets";
import GridLayout from "react-grid-layout";
import styled from "styled-components";
import { Responsive, WidthProvider } from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';
import 'react-resizable/css/styles.css';

import "./App.css";

const ResponsiveGridLayout = WidthProvider(Responsive);

function getRandomColor() {
  // Generate random values for red, green, and blue
  var red = Math.floor(Math.random() * 256);
  var green = Math.floor(Math.random() * 256);
  var blue = Math.floor(Math.random() * 256);

  // Convert the decimal values to hexadecimal
  var redHex = red.toString(16).padStart(2, '0');
  var greenHex = green.toString(16).padStart(2, '0');
  var blueHex = blue.toString(16).padStart(2, '0');

  // Create the color string by combining the hexadecimal values
  var color = '#' + redHex + greenHex + blueHex;
  
  return color;
}


const NewspaperLayout = () => {
  const layout = [
    // perbandingan: 1 4 1 utk jadi 6...harusnya??? 1.5 3 1.5
    { i: 'item1', x: 1.5*0, y: 0, w: 1.5, h: 10, color: `${getRandomColor()}`, content: 'Article 1' },
    { i: 'item2', x: 1.5*1, y: 1, w: 3, h: 10, color: `${getRandomColor()}`, content: 'Article 2' },
    { i: 'item3', x: 1.5*3, y: 2, w: 1.5, h: 10, color: `${getRandomColor()}`, content: 'Article 3' },

    { i: 'item4', x: 0+(6/5*0), y: 3, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 4' },
    { i: 'item5', x: 0+(6/5*1), y: 3, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 5' },
    { i: 'item6', x: 0+(6/5*2), y: 3, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 6' },
    { i: 'item7', x: 0+(6/5*3), y: 3, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 7' },

    { i: 'item8', x: 0+(6/5*0), y: 4, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 8' },
    { i: 'item9', x: (6/5*1), y: 4, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 9' },
    { i: 'item10', x: (6/5*2), y: 4, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 10' },
    { i: 'item11', x: (6/5*3), y: 4, w: 6/5, h: 1, color: `${getRandomColor()}`, content: 'Article 11' },

    { i: 'item12', x: 0+(6/5*4), y: 3, w: 6/5, h: 2, color: `${getRandomColor()}`, content: 'Article 12' },



    { i: 'item99', x: 0, y: 5, w: 6, h: 3, color: `${getRandomColor()}`, content: 'Static Article at Bottom', isDraggable: false, isResizable: false  },
  ];

  return (
    <GridLayout className="layout" layout={layout} cols={6} rowHeight={100} width={1200}>
      {layout.map((item) => (
        <div key={item.i} style={{ backgroundColor: item.color }}>
          {item.content}
        </div>
      ))}
    </GridLayout>
  );
}

export default NewspaperLayout;
--#
