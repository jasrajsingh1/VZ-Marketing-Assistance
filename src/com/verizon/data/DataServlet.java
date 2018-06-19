package com.verizon.data;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.verizon.util.JSONUtil;
import com.verizon.model.DataEntry;

@WebServlet("/data")
public class DataServlet extends HttpServlet{

	private static final long serialVersionUID = 1L;

	private static final String DB_URL = "jdbc:mysql://localhost/TEST";
	private static final String USER = "";
	private static final String PASS = "";
	private static final String JDBC_DRIVER = "org.postgresql.Driver";

	public void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {

		//Writer for the response.
		PrintWriter out = res.getWriter();
		
		//Declare variables.
		Connection conn = null;
		Statement stmt = null;
		ArrayList<DataEntry> de = new ArrayList<>();

		try{
			//Register JDBC driver.
			Class.forName(JDBC_DRIVER);

			//Open a connection.
			conn = DriverManager.getConnection(DB_URL,USER,PASS);

			//Execute a query.
			stmt = conn.createStatement();
			String sql = "";
			ResultSet rs = stmt.executeQuery(sql);
			
			//Extract data from result set.
			while(rs.next()) {
				de.add(new DataEntry(
						rs.getString("zipcode"),
						rs.getDouble("age"),
						rs.getString("race"),
						rs.getDouble("income"),
						rs.getInt("population")
				));

			}
			
			//Clean-up environment
			rs.close();
			stmt.close();
			conn.close();
			
		} catch(SQLException se){
			//Handle errors for JDBC
			se.printStackTrace();
		} catch(Exception e){
			//Handle errors for Class.forName
			e.printStackTrace();
		} finally {

			try{
				if(stmt != null) stmt.close();
			} catch(SQLException sqle){
				// nothing we can do
			}
			try{
				if(conn != null) conn.close();	
			} catch(SQLException se){
				se.printStackTrace();
			}
		}

		//Set content to JSON and encoding to utf-8.
		res.setContentType("application/json");
		res.setCharacterEncoding("utf-8");

		//Convert data to JSON.
		String JSONStr = JSONUtil.convertJavaToJSON(de);

		//Send data to client.
		out.write(JSONStr);
	}
}
