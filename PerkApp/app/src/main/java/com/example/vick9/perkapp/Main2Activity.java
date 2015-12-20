package com.example.vick9.perkapp;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Main2Activity extends AppCompatActivity {

    TextView currentip;
    EditText newip;
    Button saveButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        currentip = (TextView)findViewById(R.id.currentip);
        newip = (EditText)findViewById(R.id.newip);
        saveButton = (Button) findViewById(R.id.save_button);
        final SharedPreferences sharedPreferences = getApplicationContext().getSharedPreferences("myPrefs", MODE_PRIVATE);
        String ip=sharedPreferences.getString("ip", "not found");
        final SharedPreferences.Editor editor = sharedPreferences.edit();
        currentip.setText(ip);
        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                editor.putString("ip",newip.getText().toString()).commit();
                String ip=sharedPreferences.getString("ip", "not found");
                currentip.setText(ip);
            }
        });

    }

}
