import React from "react"
import { StaticQuery, graphql } from "gatsby"
import Lightbox from "./lightbox"

const Briefly = () => (
  <StaticQuery
    query={graphql`
      query {
        brieflyImages: allFile(
          filter: { sourceInstanceName: { eq: "briefly" } }
        ) {
          edges {
            node {
              childImageSharp {
                fluid(maxWidth: 2000) {
                  ...GatsbyImageSharpFluid
                }
              }
            }
          }
        }
      }
    `}
    render={data => <Lightbox brieflyImages={data.brieflyImages.edges} />}
  />
)

export default Briefly
