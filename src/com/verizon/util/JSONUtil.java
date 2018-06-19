package com.verizon.util;

import java.io.IOException;
import org.codehaus.jackson.JsonGenerationException;
import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;

public class JSONUtil {
	private static ObjectMapper mapper;
	
	static {
		mapper = new ObjectMapper();
	}
	
	public static String convertJavaToJSON(Object object) {
		String JSONStr = "";
		try {
			JSONStr = mapper.writeValueAsString(object);
		} catch (JsonGenerationException e) {
			System.out.println("Exception occured when converting Java Object to JSON: " + e.getMessage());
		} catch (JsonMappingException e) {
			System.out.println("Exception occured when converting Java Object to JSON: " + e.getMessage());
		} catch (IOException e) {
			System.out.println("Exception occured when converting Java Object to JSON: " + e.getMessage());
		}
		
		return JSONStr;
	}
	
	public static <T> T convertJSONToJava(String JSONStr, Class<T> className) {
		T result = null;
		try {
			result = mapper.readValue(JSONStr, className);
		} catch (JsonParseException e) {
			System.out.println("Exception occured when converting JSON to Java Object (Parse): " + e.getMessage());
		} catch (JsonMappingException e) {
			System.out.println("Exception occured when converting JSON to Java Object (Mapping): " + e.getMessage());
		} catch (IOException e) {
			System.out.println("Exception occured when converting JSON to Java Object (IO): " + e.getMessage());
		}
		
		return result;		
	}
	
}
