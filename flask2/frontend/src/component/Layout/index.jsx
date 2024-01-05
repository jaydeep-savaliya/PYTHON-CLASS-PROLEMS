import { Children } from "react"
import Header from "../Header"

export const Layout = ({ children }) => {
    return (
        <>
            <Header />
            <main className="container p-4">
                {children}
            </main>
        </>
    )
}
export default Layout